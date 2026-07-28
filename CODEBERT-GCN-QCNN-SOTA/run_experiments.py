#!/usr/bin/env python3
"""Run the CodeBERT-GCN-RFEMLP self-attentive QCNN reconstruction."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import torch
from torch.utils.data import DataLoader, TensorDataset

from common import (
    DATASETS, SEEDS, SPLIT_SEED, binary_metrics, fixed_manifest, load_records,
    manifest_hash, rare_cwes, set_seed,
)
from feature_extractors import prepare_feature_bundle
from model import SelfAttentiveQCNN


@torch.no_grad()
def predict(model, sequence, graph, labels, indices, batch_size):
    model.eval()
    dataset = TensorDataset(sequence[indices], graph[indices], labels[indices])
    logits, targets = [], []
    for sequence_batch, graph_batch, label_batch in DataLoader(
        dataset, batch_size=batch_size
    ):
        logits.append(model(sequence_batch, graph_batch).cpu())
        targets.append(label_batch.cpu())
    return torch.cat(logits), torch.cat(targets)


def fit_qcnn(args, bundle, seed, directory):
    directory.mkdir(parents=True, exist_ok=True)
    source = bundle["source"]
    sequence = bundle["sequence"][source]
    graph = bundle["graph"][source]
    labels = bundle["labels"][source]
    train_indices = bundle["train_indices"]
    validation_indices = bundle["validation_indices"]
    set_seed(seed)
    model = SelfAttentiveQCNN(
        sequence_dim=sequence.shape[1],
        graph_dim=graph.shape[1],
        quantum_depth=args.quantum_depth,
        attention_dim=args.attention_dim,
        attention_heads=args.attention_heads,
        dropout=0.3,
        quantum_device=args.quantum_device,
    )
    optimizer = torch.optim.SGD(
        model.parameters(), lr=0.005, momentum=0.9
    )
    checkpoint = directory / "checkpoint.pt"
    start, best, best_state, history = 0, -1.0, None, []
    if checkpoint.is_file():
        saved = torch.load(checkpoint, map_location="cpu", weights_only=False)
        model.load_state_dict(saved["model"])
        optimizer.load_state_dict(saved["optimizer"])
        start, best = saved["epoch"] + 1, saved["best"]
        best_state, history = saved["best_state"], saved["history"]
    generator = torch.Generator().manual_seed(seed)
    train_data = TensorDataset(
        sequence[train_indices], graph[train_indices], labels[train_indices]
    )
    for epoch in range(start, args.qcnn_epochs):
        model.train()
        total_loss, total = 0.0, 0
        for sequence_batch, graph_batch, label_batch in DataLoader(
            train_data, batch_size=args.qcnn_batch_size, shuffle=True,
            generator=generator,
        ):
            optimizer.zero_grad(set_to_none=True)
            loss = torch.nn.functional.cross_entropy(
                model(sequence_batch, graph_batch), label_batch
            )
            loss.backward()
            optimizer.step()
            total_loss += float(loss.detach()) * len(label_batch)
            total += len(label_batch)
        logits, target = predict(
            model, sequence, graph, labels, validation_indices,
            args.qcnn_batch_size,
        )
        metrics = binary_metrics(logits, target)
        if metrics["vulnerable_recall"] > best:
            best = metrics["vulnerable_recall"]
            best_state = {
                name: value.detach().cpu().clone()
                for name, value in model.state_dict().items()
            }
        history.append({
            "epoch": epoch + 1,
            "train_loss": total_loss / max(1, total),
            "validation": metrics,
        })
        torch.save({
            "epoch": epoch, "model": model.state_dict(),
            "optimizer": optimizer.state_dict(), "best": best,
            "best_state": best_state, "history": history,
        }, checkpoint)
        print(
            f"QCNN epoch={epoch + 1}/{args.qcnn_epochs} "
            f"val_recall={metrics['vulnerable_recall']:.4f}",
            flush=True,
        )
    model.load_state_dict(best_state)
    torch.save(best_state, directory / "model.pt")
    return model, history


def report_protocol(
    args, protocol, source, seed, model, history, bundle,
    records_by_name, manifests,
):
    targets = [source] if protocol != "generalization" else [
        name for name in DATASETS if name != source
    ]
    for target in targets:
        if protocol == "generalization":
            indices = list(range(len(records_by_name[target])))
            scope = "full_target_dataset"
        else:
            indices = manifests[target]["test"]
            scope = "fixed_test_split_101"
        logits, labels = predict(
            model, bundle["sequence"][target], bundle["graph"][target],
            bundle["labels"][target], indices, args.qcnn_batch_size,
        )
        payload = {
            "architecture": "CodeBERT-GCN-RFEMLP-QCNN-self-attention",
            "reproduction_status": "declared gate-level reconstruction",
            "protocol": protocol,
            "source": source,
            "target": target,
            "training_seed": seed,
            "split_seed": SPLIT_SEED,
            "sampling_seed": (
                args.sampling_seed if protocol == "ten_percent" else None
            ),
            "training_regime": bundle["protocol"],
            "evaluation_scope": scope,
            "train_samples": len(bundle["train_indices"]),
            "validation_samples": len(bundle["validation_indices"]),
            "test_samples": len(indices),
            "source_manifest_sha256": manifest_hash(
                records_by_name[source], manifests[source]
            ),
            "reported_components": {
                "sequence": "fine-tuned microsoft/codebert-base",
                "graph": "two-layer GCN with biaffine interaction",
                "feature_selection": "decision-tree RFE followed by MLP",
                "quantum": "four-qubit RQC and reverse-MERA-style pooling",
                "pooling": "multi-head self-attention",
            },
            "declared_missing-detail_choices": {
                "rfe_features": args.rfe_features,
                "quantum_depth": args.quantum_depth,
                "quantum_measurement": "Pauli-Z on all four qubits",
                "attention_heads": args.attention_heads,
                "attention_dimension": args.attention_dim,
                "basis_binarization": "straight-through threshold at 0.5",
            },
            "metrics": binary_metrics(logits, labels),
            "history": history,
        }
        if protocol == "long_tail":
            rare = rare_cwes(
                records_by_name[source], manifests[source]["train"]
            )
            mask = torch.tensor([
                records_by_name[target][index]["label"] == 1
                and records_by_name[target][index]["cwe"] in rare
                for index in indices
            ])
            common_mask = torch.tensor([
                records_by_name[target][index]["label"] == 1
                and records_by_name[target][index]["cwe"] not in rare
                for index in indices
            ])
            payload["long_tail"] = {
                "rare_cwes": sorted(rare),
                "rare_test_samples": int(mask.sum()),
                "rare_cwe_vulnerable_recall": (
                    float((logits[mask].argmax(-1) == 1).float().mean())
                    if mask.any() else None
                ),
                "common_cwes": sorted({
                    records_by_name[target][index]["cwe"]
                    for index in indices
                    if records_by_name[target][index]["label"] == 1
                    and records_by_name[target][index]["cwe"] not in rare
                }),
                "common_test_samples": int(common_mask.sum()),
                "common_cwe_vulnerable_recall": (
                    float(
                        (logits[common_mask].argmax(-1) == 1)
                        .float()
                        .mean()
                    )
                    if common_mask.any()
                    else None
                ),
            }
        directory = args.output / protocol / source / f"seed_{seed}"
        directory.mkdir(parents=True, exist_ok=True)
        name = target if protocol == "generalization" else source
        (directory / f"report_{name}.json").write_text(
            json.dumps(payload, indent=2) + "\n", encoding="utf-8"
        )


def run(args, protocols, source, seed, records, manifests):
    regimes = {
        "full_train" if protocol != "ten_percent" else "ten_percent"
        for protocol in protocols
    }
    trained = {}
    for regime in sorted(regimes):
        bundle = prepare_feature_bundle(
            args, source, regime, seed, records, manifests
        )
        training_directory = (
            args.output / "_trained" / regime / source / f"seed_{seed}"
        )
        model, history = fit_qcnn(args, bundle, seed, training_directory)
        trained[regime] = (model, history, bundle)
    for protocol in protocols:
        regime = "ten_percent" if protocol == "ten_percent" else "full_train"
        report_protocol(
            args, protocol, source, seed, *trained[regime], records, manifests
        )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, required=True)
    parser.add_argument(
        "--protocol",
        choices=("all", "in_domain", "generalization", "ten_percent", "long_tail"),
        default="all",
    )
    parser.add_argument("--dataset", choices=("all",) + DATASETS, default="all")
    parser.add_argument("--seed", type=int, choices=SEEDS)
    parser.add_argument("--sampling-seed", type=int, default=101)
    parser.add_argument("--feature-device", default="cuda")
    parser.add_argument("--quantum-device", default="default.qubit")
    parser.add_argument("--codebert-model", default="microsoft/codebert-base")
    parser.add_argument("--max-code-length", type=int, default=256)
    parser.add_argument("--codebert-epochs", type=int, default=50)
    parser.add_argument("--codebert-batch-size", type=int, default=32)
    parser.add_argument("--codebert-learning-rate", type=float, default=1e-3)
    parser.add_argument("--codebert-patience", type=int, default=5)
    parser.add_argument("--graph-epochs", type=int, default=300)
    parser.add_argument("--graph-batch-size", type=int, default=64)
    parser.add_argument("--graph-patience", type=int, default=30)
    parser.add_argument("--rfe-features", type=int, default=32)
    parser.add_argument("--qcnn-epochs", type=int, default=50)
    parser.add_argument("--qcnn-batch-size", type=int, default=64)
    parser.add_argument("--quantum-depth", type=int, default=2)
    parser.add_argument("--attention-dim", type=int, default=16)
    parser.add_argument("--attention-heads", type=int, default=2)
    parser.add_argument("--cache", type=Path, default=Path("cache"))
    parser.add_argument("--feature-cache", type=Path, default=Path("feature_cache"))
    parser.add_argument("--output", type=Path, default=Path("results"))
    args = parser.parse_args()
    selected = DATASETS if args.dataset == "all" else (args.dataset,)
    seeds = SEEDS if args.seed is None else (args.seed,)
    protocols = (
        ("in_domain", "generalization", "ten_percent", "long_tail")
        if args.protocol == "all" else (args.protocol,)
    )
    records = {
        name: load_records(args.repo_root, name, args.cache) for name in DATASETS
    }
    manifests = {
        name: fixed_manifest(records[name], args.cache, name) for name in DATASETS
    }
    for source in selected:
        for seed in seeds:
            run(args, protocols, source, seed, records, manifests)


if __name__ == "__main__":
    main()
