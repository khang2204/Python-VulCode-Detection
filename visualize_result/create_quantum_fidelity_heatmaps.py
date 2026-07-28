#!/usr/bin/env python3
"""Create fidelity-kernel heatmaps from the completed quantum PAG-Vul run.

The saved GAT encoder produces graph embeddings.  Each embedding is then
passed through the trained quantum *key* feature map, and the figure contains
pairwise state fidelity |<psi_i|psi_j>|^2.  This is inference only.
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
import pennylane as qml
import torch


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from train_pagvul_binary import BinaryPAG, Config  # noqa: E402
from train_pagvul_quantum import GATWarmup, GraphEncoder, extract_embeddings  # noqa: E402


def load_models(run: Path, config: Config, graphs: list) -> tuple[GraphEncoder, BinaryPAG]:
    encoder = GraphEncoder(
        int(graphs[0].x.size(1)),
        config.hidden_dim,
        config.embedding_dim,
        config.gat_layers,
        config.gat_heads,
        config.dropout,
    )
    warmup = GATWarmup(encoder, 2)
    warmup_state = torch.load(run / "gat_warmup_best.pt", map_location="cpu", weights_only=False)
    warmup.load_state_dict(warmup_state["state_dict"])
    warmup.encoder.eval()

    checkpoint = torch.load(run / "pagvul_binary_best.pt", map_location="cpu", weights_only=False)
    model = BinaryPAG(config, checkpoint["state_dict"]["prototypes"])
    model.load_state_dict(checkpoint["state_dict"])
    model.eval()
    return warmup.encoder, model


def statevector_circuit(n_qubits: int, depth: int):
    device = qml.device("default.qubit", wires=n_qubits)

    @qml.qnode(device, interface="torch", diff_method=None)
    def circuit(inputs: torch.Tensor, weights: torch.Tensor):
        for wire in range(n_qubits):
            qml.RX(inputs[wire], wires=wire)
        for layer in range(depth):
            for wire in range(n_qubits):
                qml.RY(weights[layer, wire, 0], wires=wire)
                qml.RZ(weights[layer, wire, 1], wires=wire)
            for wire in range(n_qubits):
                qml.CNOT(wires=[wire, (wire + 1) % n_qubits])
        return qml.state()

    return circuit


@torch.no_grad()
def fidelities(embeddings: torch.Tensor, model: BinaryPAG, config: Config) -> np.ndarray:
    key_map = model.attention.key
    circuit = statevector_circuit(config.n_qubits, config.quantum_depth)
    states = []
    for embedding in embeddings:
        angles = torch.tanh(key_map.pre_projection(embedding)) * torch.pi
        state = circuit(angles, key_map.q_weights)
        states.append(torch.as_tensor(state, dtype=torch.complex64))
    matrix = torch.stack(states)
    return (matrix @ matrix.conj().transpose(0, 1)).abs().square().cpu().numpy()


def plot(fidelity: np.ndarray, labels: np.ndarray, fold_name: str, output: Path, dataset_label: str) -> None:
    order = np.argsort(labels, kind="stable")
    fidelity = fidelity[order][:, order]
    labels = labels[order]
    benign_count = int((labels == 0).sum())
    figure, axis = plt.subplots(figsize=(7.4, 6.6), dpi=220)
    image = axis.imshow(fidelity, cmap="viridis", vmin=0.0, vmax=1.0, interpolation="nearest")
    if 0 < benign_count < len(labels):
        divider = benign_count - 0.5
        axis.axhline(divider, color="white", linewidth=0.7, alpha=0.75)
        axis.axvline(divider, color="white", linewidth=0.7, alpha=0.75)
    axis.set_title(f"{dataset_label} — Quantum fidelity kernel ({fold_name}, n={len(labels)})", weight="bold")
    axis.set_xlabel("Samples ordered: benign → vulnerable")
    axis.set_ylabel("Samples ordered: benign → vulnerable")
    axis.set_xticks([])
    axis.set_yticks([])
    colorbar = figure.colorbar(image, ax=axis, fraction=0.046, pad=0.04)
    colorbar.set_label(r"Fidelity $|\langle\psi_i|\psi_j\rangle|^2$")
    figure.tight_layout()
    figure.savefig(output, bbox_inches="tight")
    plt.close(figure)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run", type=Path, default=ROOT / "kaggle_deploy/in_domain/benchmarkpython/runs/20260712-015721/output/pagvul_binary_quantum")
    parser.add_argument("--dataset", type=Path, default=ROOT / "artifacts/benchmarkpython_binary_pyg/benchmarkpython_binary_graphs.pt")
    parser.add_argument("--output", type=Path, default=Path(__file__).resolve().parent / "BenchmarkPython/quantum")
    parser.add_argument("--dataset-label", default="BenchmarkPython")
    args = parser.parse_args()
    report = json.loads((args.run / "report.json").read_text(encoding="utf-8"))
    config = Config(**report["config"])
    manifests = json.loads((args.run / "split_manifest.json").read_text(encoding="utf-8"))
    graphs = torch.load(args.dataset, map_location="cpu", weights_only=False)
    encoder, model = load_models(args.run, config, graphs)
    embeddings, labels, files = extract_embeddings(encoder, graphs, config.batch_size, torch.device("cpu"))
    fold_by_file = {
        sample_file: fold
        for fold, sample_files in manifests.items()
        for sample_file in sample_files
    }
    folds = np.asarray([fold_by_file[str(sample_file)] for sample_file in files])
    classes = labels.numpy()
    args.output.mkdir(parents=True, exist_ok=True)
    for fold_name, mask in (
        ("all", np.ones(len(graphs), dtype=bool)),
        ("train", folds == "train"),
        ("validation", folds == "validation"),
        ("test", folds == "test"),
    ):
        print(f"Calculating {fold_name} fidelity matrix for {int(mask.sum())} samples...", flush=True)
        fidelity = fidelities(embeddings[mask], model, config)
        plot(fidelity, classes[mask], fold_name, args.output / f"quantum_fidelity_{fold_name}.png", args.dataset_label)
    print("Created 4 quantum fidelity heatmaps in", args.output)


if __name__ == "__main__":
    main()
