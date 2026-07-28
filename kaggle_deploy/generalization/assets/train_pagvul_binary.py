#!/usr/bin/env python3
"""Train BenchmarkPython PAG-Vul as binary detection with CWE-aware prototypes.

The classifier target is strictly ``benign (0)`` versus ``vulnerable (1)``.
CWE values are never output classes: K-Means makes prototypes for the most
frequent vulnerable CWEs and a separate benign prototype set.  This follows the
strategy used by the teammate's PyCode-Vul implementation while retaining this
repository's Joern/PyG BenchmarkPython pipeline.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from dataclasses import asdict, dataclass
from pathlib import Path

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch_geometric.loader import DataLoader

from train_pagvul_quantum import (
    GATWarmup,
    GraphEncoder,
    QuantumCrossAttention,
    class_weights,
    extract_embeddings,
    kmeans,
    parse_device,
    set_seed,
    stratified_split,
    train_classifier,
)
from train_pagvul_classical import ClassicalCrossAttention


@dataclass(frozen=True)
class Config:
    train_ratio: float
    val_ratio: float
    seed: int
    split_seed: int
    hidden_dim: int
    embedding_dim: int
    attention_dim: int
    value_dim: int
    gat_layers: int
    gat_heads: int
    dropout: float
    warmup_epochs: int
    head_epochs: int
    batch_size: int
    learning_rate: float
    head_learning_rate: float
    weight_decay: float
    top_cwes: int
    prototypes_per_cwe: int
    benign_prototypes: int
    attention: str
    n_qubits: int
    quantum_depth: int
    quantum_device: str


class BinaryHead(nn.Module):
    def __init__(self, embedding_dim: int, value_dim: int, hidden_dim: int, dropout: float):
        super().__init__()
        self.retrieved_projection = nn.Linear(value_dim, embedding_dim)
        self.fusion = nn.Sequential(
            nn.Linear(embedding_dim * 4, hidden_dim * 2),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_dim * 2, 2),
        )

    def forward(self, q: torch.Tensor, retrieved: torch.Tensor) -> torch.Tensor:
        r = self.retrieved_projection(retrieved)
        return self.fusion(torch.cat([q, r, q - r, q * r], dim=-1))


class BinaryPAG(nn.Module):
    def __init__(self, config: Config, prototypes: torch.Tensor):
        super().__init__()
        if config.attention == "classical":
            self.attention = ClassicalCrossAttention(config.embedding_dim, config.attention_dim, config.value_dim)
        else:
            self.attention = QuantumCrossAttention(
                config.embedding_dim,
                config.attention_dim,
                config.value_dim,
                config.n_qubits,
                config.quantum_depth,
                config.quantum_device,
            )
        self.head = BinaryHead(config.embedding_dim, config.value_dim, config.hidden_dim, config.dropout)
        self.register_buffer("prototypes", prototypes)

    def forward(self, q: torch.Tensor) -> tuple[torch.Tensor, torch.Tensor]:
        retrieved, weights = self.attention(q, self.prototypes)
        return self.head(q, retrieved), weights


def build_binary_prototypes(
    embeddings: torch.Tensor,
    labels: torch.Tensor,
    cwes: list[str],
    top_cwes: int,
    prototypes_per_cwe: int,
    benign_prototypes: int,
    seed: int,
) -> tuple[torch.Tensor, list[dict[str, int | str]]]:
    """K-Means training embeddings only; positive centroids retain CWE provenance."""
    if int((labels == 0).sum()) < benign_prototypes:
        raise RuntimeError("Not enough benign training samples for --benign-prototypes.")
    positive_cwes = [cwe for cwe, label in zip(cwes, labels.tolist()) if label == 1]
    ranked = Counter(positive_cwes).most_common(top_cwes)
    prototypes = [kmeans(embeddings[labels == 0], benign_prototypes, iterations=100, seed=seed)]
    manifest: list[dict[str, int | str]] = [
        {"kind": "benign", "cwe": "BENIGN", "count": benign_prototypes}
    ]
    for offset, (cwe, available) in enumerate(ranked, start=1):
        if available < prototypes_per_cwe:
            continue
        mask = torch.tensor([label == 1 and sample_cwe == cwe for label, sample_cwe in zip(labels.tolist(), cwes)])
        prototypes.append(kmeans(embeddings[mask], prototypes_per_cwe, iterations=100, seed=seed + offset))
        manifest.append({"kind": "vulnerable", "cwe": cwe, "count": prototypes_per_cwe, "train_samples": available})
    if len(prototypes) == 1:
        raise RuntimeError("No vulnerable CWE has enough training samples for --prototypes-per-cwe.")
    return torch.cat(prototypes), manifest


def pair_split(
    graphs: list,
    train_ratio: float,
    val_ratio: float,
    seed: int,
) -> tuple[list, list, list]:
    """Randomly split complete before/after pairs without pair leakage.

    This intentionally shuffles *pairs*, not the two binary labels separately.
    Each retained pair has one benign and one vulnerable member, so the three
    resulting splits remain balanced as a consequence of the data format.
    """
    if not 0 < train_ratio < 1 or not 0 < val_ratio < 1 or train_ratio + val_ratio >= 1:
        raise ValueError("train_ratio and val_ratio must be positive and sum to less than one")
    pairs: dict[str, list] = {}
    for graph in graphs:
        if not hasattr(graph, "pair_id"):
            raise RuntimeError("--split-mode pair requires pair_id metadata on every graph.")
        pairs.setdefault(str(graph.pair_id), []).append(graph)
    malformed = {
        pair_id: members
        for pair_id, members in pairs.items()
        if len(members) != 2 or {int(member.y.item()) for member in members} != {0, 1}
    }
    if malformed:
        preview = ", ".join(sorted(malformed)[:5])
        raise RuntimeError(f"Pair split requires exactly one benign and one vulnerable graph per pair; invalid: {preview}")
    pair_ids = sorted(pairs)
    generator = torch.Generator().manual_seed(seed)
    shuffled = [pair_ids[index] for index in torch.randperm(len(pair_ids), generator=generator).tolist()]
    n_val = max(1, round(len(shuffled) * val_ratio))
    n_test = max(1, round(len(shuffled) * (1 - train_ratio - val_ratio)))
    n_train = len(shuffled) - n_val - n_test
    if n_train < 1:
        raise RuntimeError("Too few pairs for the requested 3-way split.")

    def collect(ids: list[str]) -> list:
        return [graph for pair_id in ids for graph in sorted(pairs[pair_id], key=lambda item: str(item.sample_file))]

    return (
        collect(shuffled[:n_train]),
        collect(shuffled[n_train : n_train + n_val]),
        collect(shuffled[n_train + n_val :]),
    )


def binary_metrics(logits: torch.Tensor, labels: torch.Tensor) -> dict[str, float | list[list[int]]]:
    predicted = logits.argmax(dim=-1)
    tn = int(((predicted == 0) & (labels == 0)).sum())
    fp = int(((predicted == 1) & (labels == 0)).sum())
    fn = int(((predicted == 0) & (labels == 1)).sum())
    tp = int(((predicted == 1) & (labels == 1)).sum())
    precision = tp / max(1, tp + fp)
    recall = tp / max(1, tp + fn)
    specificity = tn / max(1, tn + fp)
    f1 = 2 * precision * recall / max(1e-12, precision + recall)
    return {
        "accuracy": (tp + tn) / max(1, tp + tn + fp + fn),
        "balanced_accuracy": (recall + specificity) / 2,
        "precision": precision,
        "recall": recall,
        "f1": f1,
        "confusion_matrix": [[tn, fp], [fn, tp]],
    }


@torch.no_grad()
def evaluate(model: BinaryPAG, queries: torch.Tensor, labels: torch.Tensor, device: torch.device) -> dict[str, float | list[list[int]]]:
    model.eval()
    logits, _ = model(queries.to(device))
    return binary_metrics(logits.cpu(), labels.cpu())


def train_head(
    model: BinaryPAG,
    q_train: torch.Tensor,
    y_train: torch.Tensor,
    q_val: torch.Tensor,
    y_val: torch.Tensor,
    weights: torch.Tensor,
    config: Config,
    device: torch.device,
) -> tuple[BinaryPAG, list[dict[str, float | list[list[int]]]]]:
    q_train, y_train = q_train.to(device), y_train.to(device)
    q_val, y_val = q_val.to(device), y_val.to(device)
    optimizer = torch.optim.AdamW(model.parameters(), lr=config.head_learning_rate, weight_decay=config.weight_decay)
    best_f1, best_state, history = -1.0, None, []
    for epoch in range(1, config.head_epochs + 1):
        model.train()
        optimizer.zero_grad(set_to_none=True)
        logits, _ = model(q_train)
        loss = F.cross_entropy(logits, y_train, weight=weights)
        loss.backward()
        optimizer.step()
        metrics = evaluate(model, q_val, y_val, device)
        metrics.update({"epoch": epoch, "train_loss": float(loss.item())})
        history.append(metrics)
        if float(metrics["f1"]) > best_f1:
            best_f1 = float(metrics["f1"])
            best_state = {name: value.detach().cpu().clone() for name, value in model.state_dict().items()}
    if best_state is None:
        raise RuntimeError("Binary PAG head did not produce a checkpoint.")
    model.load_state_dict(best_state)
    return model, history


def main() -> int:
    root = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--dataset", type=Path, default=root / "artifacts" / "benchmarkpython_binary_pyg" / "benchmarkpython_binary_graphs.pt")
    parser.add_argument("--out-dir", type=Path, default=root / "artifacts" / "pagvul_binary")
    parser.add_argument("--device", default="auto")
    parser.add_argument("--train-ratio", type=float, default=0.70)
    parser.add_argument("--val-ratio", type=float, default=0.15)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument(
        "--split-seed",
        type=int,
        default=42,
        help="Fixed seed used only to construct the train/validation/test split.",
    )
    parser.add_argument(
        "--split-mode",
        choices=("auto", "standard", "pair"),
        default="auto",
        help="auto uses pair-level splitting when every graph has pair_id; otherwise standard binary stratification.",
    )
    parser.add_argument("--hidden-dim", type=int, default=128)
    parser.add_argument("--embedding-dim", type=int, default=128)
    parser.add_argument("--attention-dim", type=int, default=64)
    parser.add_argument("--value-dim", type=int, default=64)
    parser.add_argument("--gat-layers", type=int, default=3)
    parser.add_argument("--gat-heads", type=int, default=4)
    parser.add_argument("--dropout", type=float, default=0.30)
    parser.add_argument("--warmup-epochs", type=int, default=50)
    parser.add_argument("--head-epochs", type=int, default=50)
    parser.add_argument("--batch-size", type=int, default=16)
    parser.add_argument("--learning-rate", type=float, default=2e-3)
    parser.add_argument("--head-learning-rate", type=float, default=2e-3)
    parser.add_argument("--weight-decay", type=float, default=1e-4)
    parser.add_argument("--top-cwes", type=int, default=6)
    parser.add_argument("--prototypes-per-cwe", type=int, default=3)
    parser.add_argument("--benign-prototypes", type=int, default=4)
    parser.add_argument("--attention", choices=("classical", "quantum"), default="classical")
    parser.add_argument("--n-qubits", type=int, default=10)
    parser.add_argument("--quantum-depth", type=int, default=5)
    parser.add_argument("--quantum-device", default="default.qubit")
    args = parser.parse_args()
    if not args.dataset.is_file():
        raise SystemExit(f"Missing dataset: {args.dataset}. Run export_benchmarkpython_pyg.py first.")
    config = Config(**{name: getattr(args, name) for name in Config.__dataclass_fields__})
    if config.top_cwes < 1 or config.prototypes_per_cwe < 1 or config.benign_prototypes < 1:
        raise SystemExit("Prototype counts and --top-cwes must be positive.")

    device = parse_device(args.device)
    set_seed(config.seed)
    torch.set_float32_matmul_precision("high")
    out_dir = args.out_dir.resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    graphs = torch.load(args.dataset, weights_only=False)
    if not graphs or any(not hasattr(graph, "is_vulnerable") for graph in graphs):
        raise SystemExit("Dataset lacks binary metadata; regenerate it with export_benchmarkpython_pyg.py.")
    if {int(graph.y.item()) for graph in graphs} != {0, 1}:
        raise SystemExit("Dataset must contain both binary labels.")

    pair_available = all(hasattr(graph, "pair_id") for graph in graphs)
    if args.split_mode == "pair" or (args.split_mode == "auto" and pair_available):
        if not pair_available:
            raise SystemExit("--split-mode pair was requested but this dataset has no pair_id metadata.")
        split_mode = "pair"
        train_graphs, val_graphs, test_graphs = pair_split(graphs, config.train_ratio, config.val_ratio, config.split_seed)
    else:
        split_mode = "standard"
        train_graphs, val_graphs, test_graphs = stratified_split(graphs, config.train_ratio, config.val_ratio, config.split_seed)
    train_loader = DataLoader(train_graphs, batch_size=config.batch_size, shuffle=True)
    val_loader = DataLoader(val_graphs, batch_size=config.batch_size, shuffle=False)
    weights = class_weights(train_graphs, 2, device)
    encoder = GraphEncoder(int(graphs[0].x.size(1)), config.hidden_dim, config.embedding_dim, config.gat_layers, config.gat_heads, config.dropout)
    warmup = GATWarmup(encoder, 2).to(device)
    warmup_history = train_classifier(
        warmup, train_loader, val_loader, 2, device, config.warmup_epochs, config.learning_rate,
        config.weight_decay, weights, out_dir / "gat_warmup_best.pt"
    )

    # Freeze a validated binary encoder before building/training prototype attention.
    for parameter in warmup.encoder.parameters():
        parameter.requires_grad_(False)
    warmup.encoder.eval()
    q_train, y_train, _ = extract_embeddings(warmup.encoder, train_graphs, config.batch_size, device)
    q_val, y_val, _ = extract_embeddings(warmup.encoder, val_graphs, config.batch_size, device)
    q_test, y_test, test_files = extract_embeddings(warmup.encoder, test_graphs, config.batch_size, device)
    prototypes, prototype_manifest = build_binary_prototypes(
        q_train, y_train, [str(graph.cwe) for graph in train_graphs], config.top_cwes,
        config.prototypes_per_cwe, config.benign_prototypes, config.seed,
    )
    model = BinaryPAG(config, prototypes.to(device)).to(device)
    model, head_history = train_head(model, q_train, y_train, q_val, y_val, weights, config, device)
    test_metrics = evaluate(model, q_test, y_test, device)
    model.eval()
    with torch.no_grad():
        test_logits, _ = model(q_test.to(device))
        test_probabilities = torch.softmax(test_logits, dim=-1).cpu()
        test_predictions = test_logits.argmax(dim=-1).cpu()
    prediction_rows = [
        {
            "sample_file": str(sample_file),
            "true_label": int(label),
            "predicted_label": int(prediction),
            "vulnerable_probability": float(probability[1]),
        }
        for sample_file, label, prediction, probability in zip(
            test_files, y_test.tolist(), test_predictions.tolist(), test_probabilities.tolist()
        )
    ]

    split_manifest = {
        "train": [graph.sample_file for graph in train_graphs],
        "validation": [graph.sample_file for graph in val_graphs],
        "test": [graph.sample_file for graph in test_graphs],
    }
    (out_dir / "split_manifest.json").write_text(json.dumps(split_manifest, indent=2) + "\n", encoding="utf-8")
    (out_dir / "test_predictions.json").write_text(json.dumps(prediction_rows, indent=2) + "\n", encoding="utf-8")
    torch.save({"prototypes": prototypes, "manifest": prototype_manifest}, out_dir / "prototype_memory.pt")
    torch.save({"state_dict": model.state_dict(), "config": asdict(config)}, out_dir / "pagvul_binary_best.pt")
    report = {
        "config": asdict(config),
        "split_mode": split_mode,
        "split_sizes": {"train": len(train_graphs), "validation": len(val_graphs), "test": len(test_graphs)},
        "split_binary_counts": {
            name: dict(Counter(int(graph.y.item()) for graph in split))
            for name, split in (("train", train_graphs), ("validation", val_graphs), ("test", test_graphs))
        },
        "class_weights": weights.detach().cpu().tolist(),
        "prototype_manifest": prototype_manifest,
        "prototype_shape": list(prototypes.shape),
        "warmup_last": warmup_history[-1],
        "head_last": head_history[-1],
        "test": test_metrics,
    }
    (out_dir / "report.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
