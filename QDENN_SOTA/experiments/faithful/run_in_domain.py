#!/usr/bin/env python3
"""Run fixed-split in-domain QDENN experiments with epoch resume."""
from __future__ import annotations

import argparse
import hashlib
import json
import random
import sys
from pathlib import Path

import torch
from torch.utils.data import DataLoader

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parents[2]
sys.path.insert(0, str(HERE))

from data import prepare_dataset  # noqa: E402
from models import MODELS  # noqa: E402


SEEDS = (101, 202, 303)
DATASETS = ("benchmarkpython", "vudenc", "realvuln_human")
SPLIT_SEED = 101


def set_seed(value: int) -> None:
    random.seed(value)
    torch.manual_seed(value)


def vulnerable_recall(logits: torch.Tensor, labels: torch.Tensor) -> float:
    predictions = logits.argmax(dim=-1)
    positives = labels == 1
    return float(((predictions == 1) & positives).sum() / positives.sum().clamp_min(1))


@torch.no_grad()
def evaluate(model, loader: DataLoader) -> tuple[float, float]:
    model.eval()
    logits, labels = [], []
    for values, targets in loader:
        logits.append(model(values).cpu())
        labels.append(targets.cpu())
    all_logits = torch.cat(logits)
    all_labels = torch.cat(labels)
    loss = torch.nn.functional.cross_entropy(all_logits, all_labels)
    return float(loss), vulnerable_recall(all_logits, all_labels)


def optimizer_for(model: torch.nn.Module):
    return torch.optim.SGD(
        model.parameters(), lr=0.01, momentum=0.9, weight_decay=0.0001
    )


def run_one(
    model_name: str,
    dataset_name: str,
    training_seed: int,
    output_root: Path,
    cache_dir: Path,
    epochs: int,
) -> None:
    run_dir = output_root / model_name / dataset_name / f"seed_{training_seed}"
    report_path = run_dir / "report.json"
    if report_path.exists():
        print(f"SKIP complete {model_name}/{dataset_name}/seed_{training_seed}", flush=True)
        return
    run_dir.mkdir(parents=True, exist_ok=True)

    datasets, manifest, vocab = prepare_dataset(
        REPO_ROOT, dataset_name, cache_dir, SPLIT_SEED
    )
    batch_size = 32
    train_generator = torch.Generator().manual_seed(training_seed)
    loaders = {
        "train": DataLoader(
            datasets["train"],
            batch_size=batch_size,
            shuffle=True,
            generator=train_generator,
        ),
        "validation": DataLoader(
            datasets["validation"], batch_size=batch_size, shuffle=False
        ),
        "test": DataLoader(
            datasets["test"], batch_size=batch_size, shuffle=False
        ),
    }

    set_seed(training_seed)
    model = MODELS[model_name](vocab_size=len(vocab), max_len=100).cpu()
    optimizer = optimizer_for(model)
    checkpoint_path = run_dir / "checkpoint.pt"
    start_epoch, best_recall, best_state = 0, -1.0, None
    history = []
    if checkpoint_path.exists():
        checkpoint = torch.load(checkpoint_path, map_location="cpu", weights_only=False)
        model.load_state_dict(checkpoint["model"])
        optimizer.load_state_dict(checkpoint["optimizer"])
        if "train_generator_state" in checkpoint:
            train_generator.set_state(checkpoint["train_generator_state"])
        if "torch_rng_state" in checkpoint:
            torch.set_rng_state(checkpoint["torch_rng_state"])
        if "python_rng_state" in checkpoint:
            random.setstate(checkpoint["python_rng_state"])
        start_epoch = checkpoint["epoch"] + 1
        best_recall = checkpoint["best_recall"]
        best_state = checkpoint["best_state"]
        history = checkpoint["history"]

    for epoch in range(start_epoch, epochs):
        model.train()
        running_loss, samples = 0.0, 0
        for values, labels in loaders["train"]:
            optimizer.zero_grad(set_to_none=True)
            logits = model(values)
            loss = torch.nn.functional.cross_entropy(logits, labels)
            loss.backward()
            optimizer.step()
            running_loss += float(loss.detach()) * len(labels)
            samples += len(labels)
        validation_loss, validation_recall = evaluate(model, loaders["validation"])
        if validation_recall > best_recall:
            best_recall = validation_recall
            best_state = {
                key: value.detach().cpu().clone()
                for key, value in model.state_dict().items()
            }
        history.append(
            {
                "epoch": epoch + 1,
                "train_loss": running_loss / max(samples, 1),
                "validation_loss": validation_loss,
                "validation_vulnerable_recall": validation_recall,
            }
        )
        torch.save(
            {
                "epoch": epoch,
                "model": model.state_dict(),
                "optimizer": optimizer.state_dict(),
                "best_recall": best_recall,
                "best_state": best_state,
                "history": history,
                "train_generator_state": train_generator.get_state(),
                "torch_rng_state": torch.get_rng_state(),
                "python_rng_state": random.getstate(),
            },
            checkpoint_path,
        )
        print(
            f"{model_name}/{dataset_name}/seed_{training_seed} "
            f"epoch={epoch + 1}/{epochs} val_recall={validation_recall:.4f}",
            flush=True,
        )

    model.load_state_dict(best_state)
    test_loss, test_recall = evaluate(model, loaders["test"])
    torch.save(best_state, run_dir / "model.pt")
    report = {
        "model": model_name,
        "dataset": dataset_name,
        "training_seed": training_seed,
        "split_seed": SPLIT_SEED,
        "epochs": epochs,
        "batch_size": batch_size,
        "train_samples": len(manifest["train"]),
        "validation_samples": len(manifest["validation"]),
        "test_samples": len(manifest["test"]),
        "split_manifest_sha256": hashlib.sha256(
            json.dumps(
                {
                    part: [
                        datasets[part].records[index]["sample_file"]
                        for index in manifest[part]
                    ]
                    for part in ("train", "validation", "test")
                },
                separators=(",", ":"),
            ).encode()
        ).hexdigest(),
        "vocab_size": len(vocab),
        "max_len": 100,
        "optimizer": "SGD",
        "learning_rate": 0.01,
        "fidelity_note": (
            "QDENN learning rate is not reported by the source paper; 0.01 is "
            "a declared reproduction choice."
        ),
        "test_loss": test_loss,
        "vulnerable_recall": test_recall,
        "history": history,
    }
    report_path.write_text(json.dumps(report, indent=2) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", choices=tuple(MODELS), required=True)
    parser.add_argument("--dataset", choices=DATASETS + ("all",), default="all")
    parser.add_argument("--seed", type=int, choices=SEEDS)
    parser.add_argument("--epochs", type=int, default=10)
    parser.add_argument("--output", type=Path, default=HERE / "results")
    parser.add_argument("--cache", type=Path, default=HERE / "cache")
    args = parser.parse_args()

    datasets = DATASETS if args.dataset == "all" else (args.dataset,)
    seeds = SEEDS if args.seed is None else (args.seed,)
    for dataset_name in datasets:
        for training_seed in seeds:
            run_one(
                args.model,
                dataset_name,
                training_seed,
                args.output,
                args.cache,
                args.epochs,
            )


if __name__ == "__main__":
    main()
