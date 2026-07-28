#!/usr/bin/env python3
"""Create 2D UMAP plots from the completed classical PAG-Vul encoder.

UMAP is fit using train embeddings only, then validation and test embeddings
are projected with the fitted mapper.  Labels are used only for plotting.
"""

from __future__ import annotations

import json
import sys
import argparse
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import torch
import umap


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from train_pagvul_quantum import GATWarmup, GraphEncoder, extract_embeddings  # noqa: E402


COLORS = {0: "#2a6fbb", 1: "#d1495b"}
NAMES = {0: "Benign", 1: "Vulnerable"}


def load_encoder(dataset: Path, run: Path, config: dict) -> GraphEncoder:
    graphs = torch.load(dataset, map_location="cpu", weights_only=False)
    encoder = GraphEncoder(
        int(graphs[0].x.size(1)),
        config["hidden_dim"],
        config["embedding_dim"],
        config["gat_layers"],
        config["gat_heads"],
        config["dropout"],
    )
    warmup = GATWarmup(encoder, 2)
    checkpoint = torch.load(run / "gat_warmup_best.pt", map_location="cpu", weights_only=False)
    warmup.load_state_dict(checkpoint["state_dict"])
    warmup.encoder.eval()
    return warmup.encoder


def plot(points: np.ndarray, labels: np.ndarray, title: str, output: Path) -> None:
    figure, axis = plt.subplots(figsize=(8, 6.5), dpi=180)
    for label in (0, 1):
        mask = labels == label
        axis.scatter(
            points[mask, 0],
            points[mask, 1],
            s=18,
            alpha=0.78,
            c=COLORS[label],
            edgecolors="white",
            linewidths=0.25,
            label=f"{NAMES[label]} ({int(mask.sum())})",
        )
    axis.set_title(title, weight="bold")
    axis.set_xlabel("UMAP-1")
    axis.set_ylabel("UMAP-2")
    axis.legend(frameon=True)
    axis.grid(alpha=0.18)
    figure.tight_layout()
    figure.savefig(output, bbox_inches="tight")
    plt.close(figure)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run", type=Path, default=ROOT / "kaggle_deploy/in_domain/benchmarkpython/runs/20260712-022323/output/pagvul_binary_classical")
    parser.add_argument("--dataset", type=Path, default=ROOT / "artifacts/benchmarkpython_binary_pyg/benchmarkpython_binary_graphs.pt")
    parser.add_argument("--output", type=Path, default=Path(__file__).resolve().parent / "BenchmarkPython/classical")
    parser.add_argument("--dataset-label", default="BenchmarkPython")
    args = parser.parse_args()
    report = json.loads((args.run / "report.json").read_text(encoding="utf-8"))
    manifests = json.loads((args.run / "split_manifest.json").read_text(encoding="utf-8"))
    graphs = torch.load(args.dataset, map_location="cpu", weights_only=False)
    encoder = load_encoder(args.dataset, args.run, report["config"])
    embeddings, labels, files = extract_embeddings(encoder, graphs, report["config"]["batch_size"], torch.device("cpu"))

    fold_by_file = {
        sample_file: fold
        for fold, sample_files in manifests.items()
        for sample_file in sample_files
    }
    folds = np.asarray([fold_by_file[str(sample_file)] for sample_file in files])
    vectors = embeddings.numpy()
    classes = labels.numpy()
    train = folds == "train"
    validation = folds == "validation"
    test = folds == "test"
    if not (train.any() and validation.any() and test.any()):
        raise RuntimeError("Split manifest did not map every expected fold.")

    mapper = umap.UMAP(
        n_components=2,
        n_neighbors=15,
        min_dist=0.10,
        metric="euclidean",
        random_state=42,
    )
    projected = np.empty((len(graphs), 2), dtype=np.float32)
    projected[train] = mapper.fit_transform(vectors[train])
    projected[validation] = mapper.transform(vectors[validation])
    projected[test] = mapper.transform(vectors[test])

    args.output.mkdir(parents=True, exist_ok=True)
    plot(projected, classes, f"{args.dataset_label} — Classical PAG-Vul (all samples)", args.output / "classical_umap_all.png")
    plot(projected[train], classes[train], f"{args.dataset_label} — Classical PAG-Vul (train)", args.output / "classical_umap_train.png")
    plot(projected[validation], classes[validation], f"{args.dataset_label} — Classical PAG-Vul (validation)", args.output / "classical_umap_validation.png")
    plot(projected[test], classes[test], f"{args.dataset_label} — Classical PAG-Vul (test)", args.output / "classical_umap_test.png")
    print("Created 4 UMAP plots in", args.output)


if __name__ == "__main__":
    main()
