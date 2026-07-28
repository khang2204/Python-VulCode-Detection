#!/usr/bin/env python3
"""Train PAG-Vul Quantum V2 from the prepared BenchmarkPython PyG dataset.

Implements the agreed pipeline:
  8. retain CWE classes with enough samples and choose K prototypes per class;
  9. create reproducible stratified train/validation/test splits;
 10. warm up the GAT graph encoder and produce graph embeddings q;
 11. run k-means on training q to construct prototype memory M;
 12. use VQC key/value encoders in prototype cross-attention;
 13. fine-tune and evaluate PAG-Vul Quantum V2.

Kaggle setup (GPU is optional; default.qubit is a simulator):
  pip install torch torch-geometric pennylane
  python train_pagvul_quantum.py --device cuda
"""

from __future__ import annotations

import argparse
import json
import random
from collections import Counter
from dataclasses import asdict, dataclass
from pathlib import Path

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch_geometric.loader import DataLoader
from torch_geometric.nn import GATConv, global_max_pool, global_mean_pool


@dataclass(frozen=True)
class Config:
    min_class_samples: int
    prototypes_per_class: int
    train_ratio: float
    val_ratio: float
    seed: int
    hidden_dim: int
    embedding_dim: int
    attention_dim: int
    value_dim: int
    gat_layers: int
    gat_heads: int
    dropout: float
    warmup_epochs: int
    quantum_epochs: int
    batch_size: int
    learning_rate: float
    quantum_learning_rate: float
    weight_decay: float
    lambda_comp: float
    lambda_sep: float
    separation_margin: float
    n_qubits: int
    quantum_depth: int
    quantum_device: str


def set_seed(seed: int) -> None:
    random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


def parse_device(value: str) -> torch.device:
    if value == "auto":
        return torch.device("cuda" if torch.cuda.is_available() else "cpu")
    device = torch.device(value)
    if device.type == "cuda" and not torch.cuda.is_available():
        raise SystemExit("--device cuda was requested but CUDA is unavailable")
    return device


def cwe_sort_key(value: str) -> int:
    return int(value)


def select_and_relabel(graphs: list, min_class_samples: int) -> tuple[list, dict[str, int], dict[str, int]]:
    counts = Counter(str(graph.cwe) for graph in graphs)
    selected_cwes = sorted((cwe for cwe, count in counts.items() if count >= min_class_samples), key=cwe_sort_key)
    if len(selected_cwes) < 2:
        raise RuntimeError("Fewer than two CWE classes meet --min-class-samples.")
    label_map = {cwe: index for index, cwe in enumerate(selected_cwes)}
    selected = []
    for graph in graphs:
        cwe = str(graph.cwe)
        if cwe not in label_map:
            continue
        graph.y = torch.tensor([label_map[cwe]], dtype=torch.long)
        selected.append(graph)
    return selected, label_map, {cwe: counts[cwe] for cwe in selected_cwes}


def stratified_split(graphs: list, train_ratio: float, val_ratio: float, seed: int) -> tuple[list, list, list]:
    if not 0 < train_ratio < 1 or not 0 < val_ratio < 1 or train_ratio + val_ratio >= 1:
        raise ValueError("train_ratio and val_ratio must be positive and sum to less than one")
    buckets: dict[int, list] = {}
    for graph in graphs:
        buckets.setdefault(int(graph.y.item()), []).append(graph)
    generator = torch.Generator().manual_seed(seed)
    train, validation, test = [], [], []
    for label, items in sorted(buckets.items()):
        if len(items) < 3:
            raise RuntimeError(f"Class index {label} has fewer than three samples; cannot make a 3-way split.")
        order = torch.randperm(len(items), generator=generator).tolist()
        shuffled = [items[index] for index in order]
        n_val = max(1, round(len(items) * val_ratio))
        n_test = max(1, round(len(items) * (1 - train_ratio - val_ratio)))
        n_train = len(items) - n_val - n_test
        if n_train < 1:
            raise RuntimeError(f"Class index {label} is too small for the requested split.")
        train.extend(shuffled[:n_train])
        validation.extend(shuffled[n_train : n_train + n_val])
        test.extend(shuffled[n_train + n_val :])
    return train, validation, test


class GraphEncoder(nn.Module):
    """Step 10: GAT graph encoder producing graph-level q embeddings."""

    def __init__(self, input_dim: int, hidden_dim: int, embedding_dim: int, layers: int, heads: int, dropout: float):
        super().__init__()
        if hidden_dim % heads:
            raise ValueError("hidden_dim must be divisible by gat_heads")
        if layers < 2:
            raise ValueError("gat_layers must be at least 2")
        self.dropout = dropout
        convs = [GATConv(input_dim, hidden_dim // heads, heads=heads, concat=True, dropout=dropout)]
        convs.extend(
            GATConv(hidden_dim, hidden_dim // heads, heads=heads, concat=True, dropout=dropout)
            for _ in range(layers - 2)
        )
        convs.append(GATConv(hidden_dim, embedding_dim, heads=1, concat=False, dropout=dropout))
        self.convs = nn.ModuleList(convs)
        self.readout = nn.Linear(embedding_dim * 2, embedding_dim)

    def forward(self, x: torch.Tensor, edge_index: torch.Tensor, batch: torch.Tensor) -> torch.Tensor:
        h = x
        for conv in self.convs[:-1]:
            h = F.elu(conv(h, edge_index))
            h = F.dropout(h, p=self.dropout, training=self.training)
        h = F.elu(self.convs[-1](h, edge_index))
        return self.readout(torch.cat([global_mean_pool(h, batch), global_max_pool(h, batch)], dim=-1))


class GATWarmup(nn.Module):
    def __init__(self, encoder: GraphEncoder, classes: int):
        super().__init__()
        self.encoder = encoder
        self.classifier = nn.Linear(encoder.readout.out_features, classes)

    def forward(self, batch):
        q = self.encoder(batch.x, batch.edge_index, batch.batch)
        return self.classifier(q), q


def classification_metrics(logits: torch.Tensor, labels: torch.Tensor, classes: int) -> dict[str, float]:
    prediction = logits.argmax(dim=-1)
    confusion = torch.zeros((classes, classes), dtype=torch.long)
    for truth, predicted in zip(labels.cpu(), prediction.cpu()):
        confusion[int(truth), int(predicted)] += 1
    f1 = []
    for cls in range(classes):
        tp = confusion[cls, cls].item()
        fp = confusion[:, cls].sum().item() - tp
        fn = confusion[cls, :].sum().item() - tp
        denominator = 2 * tp + fp + fn
        f1.append(0.0 if denominator == 0 else 2 * tp / denominator)
    return {
        "accuracy": float((prediction.cpu() == labels.cpu()).float().mean().item()),
        "macro_f1": sum(f1) / len(f1),
        "per_class_f1": f1,
    }


def class_weights(graphs: list, classes: int, device: torch.device) -> torch.Tensor:
    counts = torch.tensor([sum(int(graph.y.item()) == label for graph in graphs) for label in range(classes)], dtype=torch.float)
    return (counts.sum() / (classes * counts)).to(device)


def evaluate(model: nn.Module, loader: DataLoader, classes: int, device: torch.device) -> dict[str, float]:
    model.eval()
    all_logits, all_labels = [], []
    with torch.no_grad():
        for batch in loader:
            batch = batch.to(device)
            output = model(batch)
            logits = output[0]
            all_logits.append(logits.cpu())
            all_labels.append(batch.y.view(-1).cpu())
    return classification_metrics(torch.cat(all_logits), torch.cat(all_labels), classes)


def train_classifier(
    model: nn.Module,
    train_loader: DataLoader,
    val_loader: DataLoader,
    classes: int,
    device: torch.device,
    epochs: int,
    learning_rate: float,
    weight_decay: float,
    weights: torch.Tensor,
    checkpoint: Path,
    extra_loss=None,
) -> list[dict[str, float]]:
    optimizer = torch.optim.AdamW(model.parameters(), lr=learning_rate, weight_decay=weight_decay)
    best_metric, best_state, wait = -1.0, None, 0
    history = []
    for epoch in range(1, epochs + 1):
        model.train()
        total_loss, examples = 0.0, 0
        for batch in train_loader:
            batch = batch.to(device)
            optimizer.zero_grad(set_to_none=True)
            output = model(batch)
            logits, q = output[0], output[1]
            loss = F.cross_entropy(logits, batch.y.view(-1), weight=weights)
            if extra_loss is not None:
                loss = loss + extra_loss(q, batch.y.view(-1))
            loss.backward()
            optimizer.step()
            total_loss += loss.item() * batch.num_graphs
            examples += batch.num_graphs
        metrics = evaluate(model, val_loader, classes, device)
        metrics.update({"epoch": epoch, "train_loss": total_loss / max(1, examples)})
        history.append(metrics)
        if metrics["macro_f1"] > best_metric:
            best_metric, wait = metrics["macro_f1"], 0
            best_state = {name: tensor.detach().cpu().clone() for name, tensor in model.state_dict().items()}
            torch.save({"state_dict": best_state, "best_validation": metrics}, checkpoint)
        else:
            wait += 1
            if wait >= 20:
                break
    if best_state is None:
        raise RuntimeError("Training did not produce a checkpoint.")
    model.load_state_dict(best_state)
    return history


def extract_embeddings(encoder: GraphEncoder, graphs: list, batch_size: int, device: torch.device):
    encoder.eval()
    loader = DataLoader(graphs, batch_size=batch_size, shuffle=False)
    embeddings, labels, files = [], [], []
    with torch.no_grad():
        for batch in loader:
            batch = batch.to(device)
            embeddings.append(encoder(batch.x, batch.edge_index, batch.batch).cpu())
            labels.append(batch.y.view(-1).cpu())
            files.extend(batch.sample_file)
    return torch.cat(embeddings), torch.cat(labels), files


def kmeans(vectors: torch.Tensor, k: int, iterations: int, seed: int) -> torch.Tensor:
    if len(vectors) < k:
        raise RuntimeError(f"Cannot build {k} prototypes from only {len(vectors)} samples.")
    generator = torch.Generator().manual_seed(seed)
    centers = vectors[torch.randperm(len(vectors), generator=generator)[:k]].clone()
    for _ in range(iterations):
        assignments = torch.cdist(vectors, centers).argmin(dim=1)
        updated = []
        for cluster in range(k):
            members = vectors[assignments == cluster]
            updated.append(members.mean(dim=0) if len(members) else vectors[torch.randint(len(vectors), (1,), generator=generator)].squeeze(0))
        next_centers = torch.stack(updated)
        if torch.allclose(centers, next_centers, atol=1e-4):
            centers = next_centers
            break
        centers = next_centers
    return centers


def build_prototypes(embeddings: torch.Tensor, labels: torch.Tensor, classes: int, k: int, seed: int):
    prototypes, prototype_labels = [], []
    for label in range(classes):
        centers = kmeans(embeddings[labels == label], k, iterations=100, seed=seed + label)
        prototypes.append(centers)
        prototype_labels.append(torch.full((k,), label, dtype=torch.long))
    return torch.cat(prototypes), torch.cat(prototype_labels)


class QuantumKeyValueEncoder(nn.Module):
    """Hybrid VQC encoder used as Wk or Wv in PAG-Vul Quantum V2."""

    def __init__(self, input_dim: int, output_dim: int, n_qubits: int, depth: int, device_name: str):
        super().__init__()
        try:
            import pennylane as qml
        except ImportError as error:
            raise RuntimeError("PennyLane is required for Quantum V2: pip install pennylane") from error
        self.qml = qml
        self.n_qubits = n_qubits
        self.pre_projection = nn.Linear(input_dim, n_qubits)
        self.q_weights = nn.Parameter(torch.randn(depth, n_qubits, 2) * 0.01)
        self.post_projection = nn.Linear(n_qubits, output_dim)
        quantum_device = qml.device(device_name, wires=n_qubits)

        @qml.qnode(quantum_device, interface="torch", diff_method="best")
        def circuit(inputs, weights):
            for wire in range(n_qubits):
                qml.RX(inputs[wire], wires=wire)
            for layer in range(depth):
                for wire in range(n_qubits):
                    qml.RY(weights[layer, wire, 0], wires=wire)
                    qml.RZ(weights[layer, wire, 1], wires=wire)
                for wire in range(n_qubits):
                    qml.CNOT(wires=[wire, (wire + 1) % n_qubits])
            return [qml.expval(qml.PauliZ(wire)) for wire in range(n_qubits)]

        self.circuit = circuit

    def forward(self, prototypes: torch.Tensor) -> torch.Tensor:
        outputs = []
        for prototype in prototypes:
            angles = torch.tanh(self.pre_projection(prototype)) * torch.pi
            # PennyLane's default.qubit is a CPU state-vector simulator.  The
            # graph encoder can run on CUDA, but its VQC inputs and weights
            # must be copied to CPU for the circuit.  ``Tensor.to`` remains in
            # the autograd graph, so gradients still flow back to the CUDA
            # projections and quantum weights after the result returns.
            measured = self.circuit(angles.to("cpu"), self.q_weights.to("cpu"))
            if isinstance(measured, (tuple, list)):
                measured = torch.stack(tuple(measured))
            outputs.append(self.post_projection(measured.to(prototype.device, dtype=prototype.dtype)))
        return torch.stack(outputs)


class QuantumCrossAttention(nn.Module):
    """No K/V cache during training: VQC gradients remain valid every batch."""

    def __init__(self, embedding_dim: int, attention_dim: int, value_dim: int, n_qubits: int, depth: int, device_name: str):
        super().__init__()
        self.query = nn.Linear(embedding_dim, attention_dim, bias=False)
        self.key = QuantumKeyValueEncoder(embedding_dim, attention_dim, n_qubits, depth, device_name)
        self.value = QuantumKeyValueEncoder(embedding_dim, value_dim, n_qubits, depth, device_name)
        self.scale = attention_dim**0.5

    def forward(self, q: torch.Tensor, prototypes: torch.Tensor):
        key, value = self.key(prototypes), self.value(prototypes)
        attention = torch.softmax(self.query(q) @ key.transpose(0, 1) / self.scale, dim=-1)
        return attention @ value, attention


class PAGVulQuantum(nn.Module):
    def __init__(self, encoder: GraphEncoder, classes: int, prototypes: torch.Tensor, prototype_labels: torch.Tensor, config: Config):
        super().__init__()
        self.encoder = encoder
        self.cross_attention = QuantumCrossAttention(
            config.embedding_dim, config.attention_dim, config.value_dim, config.n_qubits, config.quantum_depth, config.quantum_device
        )
        self.retrieved_projection = nn.Linear(config.value_dim, config.embedding_dim)
        self.fusion = nn.Sequential(
            nn.Linear(config.embedding_dim * 4, config.hidden_dim * 2),
            nn.ReLU(),
            nn.Dropout(config.dropout),
            nn.Linear(config.hidden_dim * 2, classes),
        )
        self.register_buffer("prototypes", prototypes)
        self.register_buffer("prototype_labels", prototype_labels)

    def forward(self, batch):
        q = self.encoder(batch.x, batch.edge_index, batch.batch)
        retrieved, attention = self.cross_attention(q, self.prototypes)
        retrieved = self.retrieved_projection(retrieved)
        logits = self.fusion(torch.cat([q, retrieved, q - retrieved, q * retrieved], dim=-1))
        return logits, q, attention


def prototype_regularizer(prototypes: torch.Tensor, prototype_labels: torch.Tensor, comp_weight: float, sep_weight: float, margin: float):
    def loss(q: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
        distances = torch.cdist(q, prototypes)
        same_mask = prototype_labels.unsqueeze(0) == labels.unsqueeze(1)
        different_mask = ~same_mask
        compactness = distances.masked_fill(~same_mask, float("inf")).min(dim=1).values.pow(2).mean()
        separation = F.relu(margin - distances.masked_fill(~different_mask, float("inf")).min(dim=1).values).mean()
        return comp_weight * compactness + sep_weight * separation

    return loss


def main() -> int:
    root = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--dataset", type=Path, default=root / "artifacts" / "benchmarkpython_vuln_pyg" / "benchmarkpython_vuln_graphs.pt")
    parser.add_argument("--out-dir", type=Path, default=root / "artifacts" / "pagvul_quantum")
    parser.add_argument("--device", default="auto", help="auto, cpu, cuda, or cuda:0")
    parser.add_argument("--min-class-samples", type=int, default=20)
    parser.add_argument("--prototypes-per-class", type=int, default=5)
    parser.add_argument("--train-ratio", type=float, default=0.70)
    parser.add_argument("--val-ratio", type=float, default=0.15)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--hidden-dim", type=int, default=128)
    parser.add_argument("--embedding-dim", type=int, default=128)
    parser.add_argument("--attention-dim", type=int, default=32)
    parser.add_argument("--value-dim", type=int, default=32)
    parser.add_argument("--gat-layers", type=int, default=3)
    parser.add_argument("--gat-heads", type=int, default=4)
    parser.add_argument("--dropout", type=float, default=0.30)
    parser.add_argument("--warmup-epochs", type=int, default=50)
    parser.add_argument("--quantum-epochs", type=int, default=30)
    parser.add_argument("--batch-size", type=int, default=16)
    parser.add_argument("--learning-rate", type=float, default=2e-3)
    parser.add_argument("--quantum-learning-rate", type=float, default=2e-3)
    parser.add_argument("--weight-decay", type=float, default=1e-4)
    parser.add_argument("--lambda-comp", type=float, default=0.10)
    parser.add_argument("--lambda-sep", type=float, default=0.10)
    parser.add_argument("--separation-margin", type=float, default=1.0)
    parser.add_argument("--n-qubits", type=int, default=10)
    parser.add_argument("--quantum-depth", type=int, default=5)
    parser.add_argument("--quantum-device", default="default.qubit")
    args = parser.parse_args()

    if not args.dataset.is_file():
        raise SystemExit(f"Missing dataset: {args.dataset}")
    config = Config(**{field: getattr(args, field) for field in Config.__dataclass_fields__})
    device = parse_device(args.device)
    set_seed(config.seed)
    torch.set_float32_matmul_precision("high")
    out_dir = args.out_dir.resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    graphs = torch.load(args.dataset, weights_only=False)
    graphs, label_map, source_counts = select_and_relabel(graphs, config.min_class_samples)
    train_graphs, val_graphs, test_graphs = stratified_split(graphs, config.train_ratio, config.val_ratio, config.seed)
    classes = len(label_map)
    min_train = min(sum(int(graph.y.item()) == label for graph in train_graphs) for label in range(classes))
    if config.prototypes_per_class > min_train:
        raise SystemExit(f"K={config.prototypes_per_class} exceeds the smallest training class ({min_train}).")

    input_dim = int(graphs[0].x.size(1))
    train_loader = DataLoader(train_graphs, batch_size=config.batch_size, shuffle=True)
    val_loader = DataLoader(val_graphs, batch_size=config.batch_size, shuffle=False)
    test_loader = DataLoader(test_graphs, batch_size=config.batch_size, shuffle=False)
    weights = class_weights(train_graphs, classes, device)
    split_manifest = {
        "train": [graph.sample_file for graph in train_graphs],
        "validation": [graph.sample_file for graph in val_graphs],
        "test": [graph.sample_file for graph in test_graphs],
    }
    (out_dir / "split_manifest.json").write_text(json.dumps(split_manifest, indent=2) + "\n", encoding="utf-8")
    (out_dir / "experiment_config.json").write_text(
        json.dumps({"config": asdict(config), "device": str(device), "cwe_to_class": label_map, "source_counts": source_counts}, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    encoder = GraphEncoder(input_dim, config.hidden_dim, config.embedding_dim, config.gat_layers, config.gat_heads, config.dropout)
    warmup = GATWarmup(encoder, classes).to(device)
    warmup_history = train_classifier(
        warmup, train_loader, val_loader, classes, device, config.warmup_epochs, config.learning_rate, config.weight_decay,
        weights, out_dir / "gat_warmup_best.pt"
    )
    train_q, train_y, train_files = extract_embeddings(warmup.encoder, train_graphs, config.batch_size, device)
    prototypes, prototype_labels = build_prototypes(train_q, train_y, classes, config.prototypes_per_class, config.seed)
    torch.save({"embeddings": train_q, "labels": train_y, "sample_files": train_files}, out_dir / "train_embeddings.pt")
    torch.save({"prototypes": prototypes, "prototype_labels": prototype_labels}, out_dir / "prototype_memory.pt")

    quantum = PAGVulQuantum(warmup.encoder, classes, prototypes, prototype_labels, config).to(device)
    regularizer = prototype_regularizer(quantum.prototypes, quantum.prototype_labels, config.lambda_comp, config.lambda_sep, config.separation_margin)
    quantum_history = train_classifier(
        quantum, train_loader, val_loader, classes, device, config.quantum_epochs, config.quantum_learning_rate, config.weight_decay,
        weights, out_dir / "pagvul_quantum_best.pt", extra_loss=regularizer
    )
    test_metrics = evaluate(quantum, test_loader, classes, device)
    report = {
        "selected_graphs": len(graphs),
        "classes": classes,
        "cwe_to_class": label_map,
        "source_counts": source_counts,
        "split_sizes": {"train": len(train_graphs), "validation": len(val_graphs), "test": len(test_graphs)},
        "prototypes_shape": list(prototypes.shape),
        "warmup_last": warmup_history[-1],
        "quantum_last": quantum_history[-1],
        "test": test_metrics,
    }
    (out_dir / "report.json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
