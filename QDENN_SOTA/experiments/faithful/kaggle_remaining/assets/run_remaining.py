#!/usr/bin/env python3
"""Run QDENN generalization, ten-percent, and long-tail protocols.

Generalization and long-tail reuse the completed fixed-split-101 in-domain
models. Only ten-percent trains new models. Every report contains the full
binary metric set; long-tail additionally reports recall on rare CWE samples.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import random
import sys
from collections import Counter
from pathlib import Path

import torch
from torch.utils.data import DataLoader

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from data import TokenDataset, prepare_dataset  # noqa: E402
from models import QDENN  # noqa: E402


DATASETS = ("benchmarkpython", "vudenc", "realvuln_human")
SEEDS = (101, 202, 303)
SPLIT_SEED = 101


def set_seed(seed: int) -> None:
    random.seed(seed)
    torch.manual_seed(seed)


def binary_metrics(logits: torch.Tensor, labels: torch.Tensor) -> dict[str, float]:
    predictions = logits.argmax(-1)
    tp = int(((predictions == 1) & (labels == 1)).sum())
    tn = int(((predictions == 0) & (labels == 0)).sum())
    fp = int(((predictions == 1) & (labels == 0)).sum())
    fn = int(((predictions == 0) & (labels == 1)).sum())
    precision = tp / max(1, tp + fp)
    recall = tp / max(1, tp + fn)
    specificity = tn / max(1, tn + fp)
    return {
        "accuracy": (tp + tn) / max(1, len(labels)),
        "balanced_accuracy": 0.5 * (recall + specificity),
        "precision": precision,
        "recall": recall,
        "f1": 2 * precision * recall / max(1e-12, precision + recall),
        "vulnerable_recall": recall,
    }


@torch.no_grad()
def predict(model: QDENN, dataset: TokenDataset, batch_size: int):
    model.eval()
    logits, labels = [], []
    loader = DataLoader(dataset, batch_size=batch_size, shuffle=False)
    for batch, (values, targets) in enumerate(loader, 1):
        logits.append(model(values).cpu())
        labels.append(targets.cpu())
        if batch % 25 == 0 or batch == len(loader):
            print(f"evaluation batch={batch}/{len(loader)}", flush=True)
    return torch.cat(logits), torch.cat(labels)


def manifest_hash(dataset: TokenDataset, manifest: dict) -> str:
    value = {
        part: [
            dataset.records[index]["sample_file"]
            for index in manifest[part]
        ]
        for part in ("train", "validation", "test")
    }
    return hashlib.sha256(
        json.dumps(value, separators=(",", ":")).encode()
    ).hexdigest()


def rare_cwes(records: list[dict], train_indices: list[int]) -> set[str]:
    counts = Counter(
        records[index]["cwe"]
        for index in train_indices
        if records[index]["label"] == 1
    )
    if not counts:
        return set()
    cutoff = sorted(counts.values())[(len(counts) - 1) // 2]
    return {name for name, count in counts.items() if count <= cutoff}


def ten_percent_indices(
    records: list[dict], train_indices: list[int], seed: int
) -> list[int]:
    groups: dict[tuple[int, str], list[int]] = {}
    for index in train_indices:
        record = records[index]
        key = (
            record["label"],
            "BENIGN" if record["label"] == 0 else record["cwe"],
        )
        groups.setdefault(key, []).append(index)
    generator = torch.Generator().manual_seed(seed)
    selected = []
    for key in sorted(groups):
        members = sorted(groups[key], key=lambda index: records[index]["sample_file"])
        amount = min(len(members), max(1, round(0.1 * len(members))))
        offsets = torch.randperm(len(members), generator=generator)[:amount].tolist()
        selected.extend(members[offset] for offset in offsets)
    return sorted(selected)


def load_model(state_path: Path, vocab_size: int) -> QDENN:
    model = QDENN(vocab_size=vocab_size, max_len=100).cpu()
    model.load_state_dict(
        torch.load(state_path, map_location="cpu", weights_only=True)
    )
    return model


def train_ten_percent(
    records: list[dict],
    train_indices: list[int],
    validation_indices: list[int],
    vocab: dict,
    seed: int,
    run_dir: Path,
    epochs: int,
    batch_size: int,
) -> tuple[QDENN, list[dict]]:
    set_seed(seed)
    model = QDENN(vocab_size=len(vocab), max_len=100).cpu()
    optimizer = torch.optim.SGD(
        model.parameters(), lr=0.01, momentum=0.9, weight_decay=0.0001
    )
    train_data = TokenDataset(records, train_indices, vocab)
    validation_data = TokenDataset(records, validation_indices, vocab)
    generator = torch.Generator().manual_seed(seed)
    checkpoint = run_dir / "checkpoint.pt"
    start, best, best_state, history = 0, -1.0, None, []
    if checkpoint.is_file():
        saved = torch.load(checkpoint, map_location="cpu", weights_only=False)
        model.load_state_dict(saved["model"])
        optimizer.load_state_dict(saved["optimizer"])
        start = saved["epoch"] + 1
        best = saved["best"]
        best_state = saved["best_state"]
        history = saved["history"]
        if "generator_state" in saved:
            generator.set_state(saved["generator_state"])
    for epoch in range(start, epochs):
        model.train()
        total_loss, total = 0.0, 0
        loader = DataLoader(
            train_data,
            batch_size=batch_size,
            shuffle=True,
            generator=generator,
        )
        for values, labels in loader:
            optimizer.zero_grad(set_to_none=True)
            loss = torch.nn.functional.cross_entropy(model(values), labels)
            loss.backward()
            optimizer.step()
            total_loss += float(loss.detach()) * len(labels)
            total += len(labels)
        logits, labels = predict(model, validation_data, batch_size)
        metrics = binary_metrics(logits, labels)
        if metrics["recall"] > best:
            best = metrics["recall"]
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
            "epoch": epoch,
            "model": model.state_dict(),
            "optimizer": optimizer.state_dict(),
            "best": best,
            "best_state": best_state,
            "history": history,
            "generator_state": generator.get_state(),
        }, checkpoint)
        print(
            f"ten_percent seed={seed} epoch={epoch + 1}/{epochs} "
            f"val_recall={metrics['recall']:.4f}",
            flush=True,
        )
    if best_state is None:
        raise RuntimeError("Ten-percent training produced no best model")
    model.load_state_dict(best_state)
    torch.save(best_state, run_dir / "model.pt")
    return model, history


def write_report(
    path: Path,
    protocol: str,
    source: str,
    target: str,
    seed: int,
    train_samples: int,
    validation_samples: int,
    test_indices: list[int],
    source_manifest_sha256: str,
    logits: torch.Tensor,
    labels: torch.Tensor,
    history: list[dict] | None,
    long_tail: dict | None = None,
) -> None:
    payload = {
        "architecture": "QDENN",
        "protocol": protocol,
        "source": source,
        "target": target,
        "training_seed": seed,
        "split_seed": SPLIT_SEED,
        "evaluation_scope": (
            "full_target_dataset"
            if protocol == "generalization"
            else "fixed_test_split_101"
        ),
        "train_samples": train_samples,
        "validation_samples": validation_samples,
        "test_samples": len(test_indices),
        "source_manifest_sha256": source_manifest_sha256,
        "configuration": {
            "vocabulary": 128,
            "qubits": 7,
            "max_length": 100,
            "epochs": 10,
            "batch_size": 32,
            "optimizer": "SGD",
            "learning_rate": 0.01,
            "fidelity_note": (
                "Learning rate is not reported by the source paper; 0.01 is "
                "the declared reproduction choice."
            ),
        },
        "metrics": binary_metrics(logits, labels),
    }
    if history is not None:
        payload["history"] = history
    if long_tail is not None:
        payload["long_tail"] = long_tail
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def evaluate_reused_models(args, prepared) -> None:
    for source in DATASETS:
        datasets, manifest, vocab = prepared[source]
        records = datasets["train"].records
        source_hash = manifest_hash(datasets["train"], manifest)
        rare = rare_cwes(records, manifest["train"])
        for seed in SEEDS:
            state = args.in_domain_models / source / f"seed_{seed}" / "model.pt"
            if not state.is_file():
                raise FileNotFoundError(f"Missing in-domain model: {state}")
            model = load_model(state, len(vocab))
            print(f"REUSE source={source} seed={seed}", flush=True)
            generalization_dir = (
                args.output / "generalization" / source / f"seed_{seed}"
            )
            generalization_dir.mkdir(parents=True, exist_ok=True)
            for target in DATASETS:
                if target == source:
                    continue
                target_datasets, _, _ = prepared[target]
                target_records = target_datasets["train"].records
                indices = list(range(len(target_records)))
                target_data = TokenDataset(target_records, indices, vocab)
                logits, labels = predict(model, target_data, args.batch_size)
                write_report(
                    generalization_dir / f"report_{target}.json",
                    "generalization",
                    source,
                    target,
                    seed,
                    len(manifest["train"]),
                    len(manifest["validation"]),
                    indices,
                    source_hash,
                    logits,
                    labels,
                    None,
                )
            long_tail_dir = args.output / "long_tail" / source / f"seed_{seed}"
            long_tail_dir.mkdir(parents=True, exist_ok=True)
            indices = list(manifest["test"])
            test_data = TokenDataset(records, indices, vocab)
            logits, labels = predict(model, test_data, args.batch_size)
            mask = torch.tensor([
                records[index]["label"] == 1
                and records[index]["cwe"] in rare
                for index in indices
            ])
            long_tail = {
                "rare_cwes": sorted(rare),
                "rare_test_samples": int(mask.sum()),
                "rare_cwe_vulnerable_recall": (
                    float((logits[mask].argmax(-1) == 1).float().mean())
                    if mask.any()
                    else None
                ),
            }
            write_report(
                long_tail_dir / f"report_{source}.json",
                "long_tail",
                source,
                source,
                seed,
                len(manifest["train"]),
                len(manifest["validation"]),
                indices,
                source_hash,
                logits,
                labels,
                None,
                long_tail,
            )


def run_ten_percent(args, prepared) -> None:
    for source in DATASETS:
        datasets, manifest, vocab = prepared[source]
        records = datasets["train"].records
        source_hash = manifest_hash(datasets["train"], manifest)
        for seed in SEEDS:
            selected = ten_percent_indices(records, manifest["train"], seed)
            run_dir = args.output / "ten_percent" / source / f"seed_{seed}"
            run_dir.mkdir(parents=True, exist_ok=True)
            report = run_dir / f"report_{source}.json"
            if report.is_file():
                print(f"SKIP ten_percent source={source} seed={seed}", flush=True)
                continue
            model, history = train_ten_percent(
                records,
                selected,
                manifest["validation"],
                vocab,
                seed,
                run_dir,
                args.epochs,
                args.batch_size,
            )
            indices = list(manifest["test"])
            logits, labels = predict(
                model,
                TokenDataset(records, indices, vocab),
                args.batch_size,
            )
            write_report(
                report,
                "ten_percent",
                source,
                source,
                seed,
                len(selected),
                len(manifest["validation"]),
                indices,
                source_hash,
                logits,
                labels,
                history,
            )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", type=Path, required=True)
    parser.add_argument("--cache", type=Path, required=True)
    parser.add_argument("--in-domain-models", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--epochs", type=int, default=10)
    parser.add_argument("--batch-size", type=int, default=32)
    args = parser.parse_args()
    prepared = {
        dataset: prepare_dataset(args.repo_root, dataset, args.cache, SPLIT_SEED)
        for dataset in DATASETS
    }
    evaluate_reused_models(args, prepared)
    run_ten_percent(args, prepared)
    print("QDENN_REMAINING_COMPLETE", flush=True)


if __name__ == "__main__":
    main()
