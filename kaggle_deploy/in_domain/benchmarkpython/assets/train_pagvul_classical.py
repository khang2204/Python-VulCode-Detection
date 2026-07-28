#!/usr/bin/env python3
"""Classical PAG-Vul baseline for steps 8--13.

This companion to ``train_pagvul_quantum.py`` keeps the same CWE selection,
stratified split, GAT warm-up, k-means prototype construction, fusion and
prototype losses. It differs only at step 12: trainable linear Wq/Wk/Wv replace
the VQC Key/Value encoders. Run it with the same seed and hyperparameters as
the Quantum script for a fair comparison.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path

import torch
import torch.nn as nn
from torch_geometric.loader import DataLoader

# Shared preprocessing, GAT, loss, k-means, and metric implementations. These
# helpers do not import or instantiate PennyLane, so this baseline needs only
# PyTorch and PyTorch Geometric.
from train_pagvul_quantum import (
    GraphEncoder,
    build_prototypes,
    class_weights,
    evaluate,
    extract_embeddings,
    parse_device,
    prototype_regularizer,
    select_and_relabel,
    set_seed,
    stratified_split,
    train_classifier,
)


@dataclass(frozen=True)
class ClassicalConfig:
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
    classical_epochs: int
    batch_size: int
    learning_rate: float
    classical_learning_rate: float
    weight_decay: float
    lambda_comp: float
    lambda_sep: float
    separation_margin: float


class ClassicalCrossAttention(nn.Module):
    """V1-style trainable linear projections of prototype memory M."""

    def __init__(self, embedding_dim: int, attention_dim: int, value_dim: int):
        super().__init__()
        self.wq = nn.Linear(embedding_dim, attention_dim, bias=False)
        self.wk = nn.Linear(embedding_dim, attention_dim, bias=False)
        self.wv = nn.Linear(embedding_dim, value_dim, bias=False)
        self.scale = attention_dim**0.5

    def forward(self, q: torch.Tensor, prototypes: torch.Tensor):
        query = self.wq(q)
        key = self.wk(prototypes)
        value = self.wv(prototypes)
        attention = torch.softmax(query @ key.transpose(0, 1) / self.scale, dim=-1)
        return attention @ value, attention


class PAGVulClassical(nn.Module):
    def __init__(self, encoder: GraphEncoder, classes: int, prototypes: torch.Tensor, prototype_labels: torch.Tensor, config: ClassicalConfig):
        super().__init__()
        self.encoder = encoder
        self.cross_attention = ClassicalCrossAttention(config.embedding_dim, config.attention_dim, config.value_dim)
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


class GATWarmup(nn.Module):
    def __init__(self, encoder: GraphEncoder, classes: int):
        super().__init__()
        self.encoder = encoder
        self.classifier = nn.Linear(encoder.readout.out_features, classes)

    def forward(self, batch):
        q = self.encoder(batch.x, batch.edge_index, batch.batch)
        return self.classifier(q), q


def main() -> int:
    root = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--dataset", type=Path, default=root / "artifacts" / "benchmarkpython_vuln_pyg" / "benchmarkpython_vuln_graphs.pt")
    parser.add_argument("--out-dir", type=Path, default=root / "artifacts" / "pagvul_classical")
    parser.add_argument("--device", default="auto")
    parser.add_argument("--min-class-samples", type=int, default=20)
    parser.add_argument("--prototypes-per-class", type=int, default=5)
    parser.add_argument("--train-ratio", type=float, default=0.70)
    parser.add_argument("--val-ratio", type=float, default=0.15)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--hidden-dim", type=int, default=128)
    parser.add_argument("--embedding-dim", type=int, default=128)
    parser.add_argument("--attention-dim", type=int, default=64)
    parser.add_argument("--value-dim", type=int, default=64)
    parser.add_argument("--gat-layers", type=int, default=3)
    parser.add_argument("--gat-heads", type=int, default=4)
    parser.add_argument("--dropout", type=float, default=0.30)
    parser.add_argument("--warmup-epochs", type=int, default=50)
    parser.add_argument("--classical-epochs", type=int, default=30)
    parser.add_argument("--batch-size", type=int, default=16)
    parser.add_argument("--learning-rate", type=float, default=2e-3)
    parser.add_argument("--classical-learning-rate", type=float, default=2e-3)
    parser.add_argument("--weight-decay", type=float, default=1e-4)
    parser.add_argument("--lambda-comp", type=float, default=0.10)
    parser.add_argument("--lambda-sep", type=float, default=0.10)
    parser.add_argument("--separation-margin", type=float, default=1.0)
    args = parser.parse_args()

    if not args.dataset.is_file():
        raise SystemExit(f"Missing dataset: {args.dataset}")
    config = ClassicalConfig(**{field: getattr(args, field) for field in ClassicalConfig.__dataclass_fields__})
    device = parse_device(args.device)
    set_seed(config.seed)
    torch.set_float32_matmul_precision("high")
    out_dir = args.out_dir.resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    graphs = torch.load(args.dataset, weights_only=False)
    graphs, cwe_to_class, source_counts = select_and_relabel(graphs, config.min_class_samples)
    train_graphs, val_graphs, test_graphs = stratified_split(graphs, config.train_ratio, config.val_ratio, config.seed)
    classes = len(cwe_to_class)
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
        json.dumps({"config": asdict(config), "device": str(device), "cwe_to_class": cwe_to_class, "source_counts": source_counts}, indent=2, sort_keys=True) + "\n",
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

    model = PAGVulClassical(warmup.encoder, classes, prototypes, prototype_labels, config).to(device)
    regularizer = prototype_regularizer(model.prototypes, model.prototype_labels, config.lambda_comp, config.lambda_sep, config.separation_margin)
    classical_history = train_classifier(
        model, train_loader, val_loader, classes, device, config.classical_epochs, config.classical_learning_rate,
        config.weight_decay, weights, out_dir / "pagvul_classical_best.pt", extra_loss=regularizer
    )
    test_metrics = evaluate(model, test_loader, classes, device)
    report = {
        "selected_graphs": len(graphs),
        "classes": classes,
        "cwe_to_class": cwe_to_class,
        "source_counts": source_counts,
        "split_sizes": {"train": len(train_graphs), "validation": len(val_graphs), "test": len(test_graphs)},
        "prototypes_shape": list(prototypes.shape),
        "warmup_last": warmup_history[-1],
        "classical_last": classical_history[-1],
        "test": test_metrics,
    }
    (out_dir / "report.json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
