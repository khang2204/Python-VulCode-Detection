#!/usr/bin/env python3
"""Evaluate saved binary PAG-Vul checkpoints across benchmark datasets."""

from __future__ import annotations

import argparse
import json
import statistics
from collections import defaultdict
from pathlib import Path

import torch

from train_pagvul_binary import BinaryPAG, Config, binary_metrics
from train_pagvul_quantum import GATWarmup, GraphEncoder, extract_embeddings


SEEDS = (101, 202, 303)
ATTENTIONS = ("classical", "quantum")
METRICS = ("accuracy", "balanced_accuracy", "precision", "recall", "f1")


def parse_graphs(values: list[str]) -> dict[str, Path]:
    graphs: dict[str, Path] = {}
    for value in values:
        name, separator, raw_path = value.partition("=")
        if not separator or not name or not raw_path:
            raise ValueError(f"Expected NAME=PATH, received {value!r}")
        path = Path(raw_path)
        if not path.is_file():
            raise FileNotFoundError(path)
        graphs[name] = path
    return graphs


def evaluate_one(graphs: list, run: Path, device: torch.device, batch_size: int) -> dict:
    checkpoint = torch.load(run / "pagvul_binary_best.pt", map_location="cpu", weights_only=False)
    config = Config(**checkpoint["config"])
    warmup_checkpoint = torch.load(run / "gat_warmup_best.pt", map_location="cpu", weights_only=False)
    encoder = GraphEncoder(
        int(graphs[0].x.size(1)), config.hidden_dim, config.embedding_dim,
        config.gat_layers, config.gat_heads, config.dropout,
    )
    warmup = GATWarmup(encoder, 2)
    warmup.load_state_dict(warmup_checkpoint["state_dict"])
    warmup.to(device).eval()
    queries, labels, _ = extract_embeddings(warmup.encoder, graphs, batch_size, device)
    prototypes = checkpoint["state_dict"]["prototypes"]
    model = BinaryPAG(config, prototypes).to(device)
    model.load_state_dict(checkpoint["state_dict"])
    model.eval()
    with torch.no_grad():
        logits, _ = model(queries.to(device))
    return binary_metrics(logits.cpu(), labels)


def mean_std(values: list[float]) -> tuple[float, float]:
    return statistics.mean(values), statistics.stdev(values) if len(values) > 1 else 0.0


def write_summary(rows: list[dict], output: Path) -> None:
    groups: dict[tuple[str, str, str], list[dict]] = defaultdict(list)
    for row in rows:
        groups[(row["source"], row["target"], row["attention"])].append(row["metrics"])
    lines = ["# Cross-benchmark generalization", "", "| Train → Test | Method | Accuracy | Bal. Acc. | Precision | Recall | F1 |", "| --- | --- | ---: | ---: | ---: | ---: | ---: |"]
    for source, target, attention in sorted(groups):
        values = groups[(source, target, attention)]
        formatted = []
        for metric in METRICS:
            average, deviation = mean_std([float(value[metric]) for value in values])
            formatted.append(f"{average * 100:.2f}% ± {deviation * 100:.2f}%")
        lines.append(f"| {source} → {target} | {attention.title()} | " + " | ".join(formatted) + " |")
    (output / "summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--graph", action="append", required=True, help="Dataset mapping NAME=PATH; repeat for each dataset.")
    parser.add_argument("--runs-root", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--device", default="cuda")
    parser.add_argument("--graph-batch-size", type=int, default=64)
    args = parser.parse_args()
    graphs_by_name = {name: torch.load(path, weights_only=False) for name, path in parse_graphs(args.graph).items()}
    device = torch.device(args.device if args.device == "cpu" or torch.cuda.is_available() else "cpu")
    rows: list[dict] = []
    for source in sorted(graphs_by_name):
        for target, graphs in sorted(graphs_by_name.items()):
            if source == target:
                continue
            for attention in ATTENTIONS:
                for seed in SEEDS:
                    run = args.runs_root / source / attention / f"seed_{seed}"
                    metrics = evaluate_one(graphs, run, device, args.graph_batch_size)
                    rows.append({"source": source, "target": target, "attention": attention, "seed": seed, "metrics": metrics})
    args.output.mkdir(parents=True, exist_ok=True)
    (args.output / "results.json").write_text(json.dumps(rows, indent=2) + "\n", encoding="utf-8")
    write_summary(rows, args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
