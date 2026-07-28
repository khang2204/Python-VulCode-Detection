#!/usr/bin/env python3
"""Run RQENN in-domain, generalization, ten-percent, and long-tail protocols."""
from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

import torch
from torch.utils.data import DataLoader, Dataset

from common import (
    DATASETS, SEEDS, SPLIT_SEED, binary_metrics, fixed_manifest, load_records,
    manifest_hash, rare_cwes, set_seed, ten_percent_indices,
)
from model import RQENN

PAD, UNK, VOCAB_SIZE, MAX_LEN = "<PAD>", "<UNK>", 128, 100


def build_vocab(records: list[dict], indices: list[int]) -> dict[str, int]:
    counts = Counter(token for index in indices for token in records[index]["tokens"])
    vocab = {PAD: 0, UNK: 1}
    for value, _ in counts.most_common(VOCAB_SIZE - 2):
        vocab[value] = len(vocab)
    return vocab


class Tokens(Dataset):
    def __init__(self, records: list[dict], indices: list[int], vocab: dict[str, int]):
        self.records, self.indices, self.vocab = records, indices, vocab

    def __len__(self):
        return len(self.indices)

    def __getitem__(self, offset):
        record = self.records[self.indices[offset]]
        values = [self.vocab.get(token, 1) for token in record["tokens"][:MAX_LEN]]
        values.extend([0] * (MAX_LEN - len(values)))
        return torch.tensor(values), torch.tensor(record["label"])


@torch.no_grad()
def predict(model, dataset, batch_size):
    model.eval()
    logits, labels = [], []
    for values, target in DataLoader(dataset, batch_size=batch_size):
        logits.append(model(values).cpu())
        labels.append(target.cpu())
    return torch.cat(logits), torch.cat(labels)


def train(
    records, train_indices, validation_indices, vocab, seed, epochs,
    batch_size, run_dir, quantum_device,
):
    set_seed(seed)
    model = RQENN(quantum_device=quantum_device)
    if model.quantum_parameter_count != 106:
        raise RuntimeError(f"RQENN parameter audit failed: {model.quantum_parameter_count}")
    optimizer = torch.optim.Adam(model.parameters(), lr=0.01)
    generator = torch.Generator().manual_seed(seed)
    train_data = Tokens(records, train_indices, vocab)
    validation_data = Tokens(records, validation_indices, vocab)
    checkpoint = run_dir / "checkpoint.pt"
    start, best, best_state, history = 0, -1.0, None, []
    if checkpoint.is_file():
        saved = torch.load(checkpoint, map_location="cpu", weights_only=False)
        model.load_state_dict(saved["model"])
        optimizer.load_state_dict(saved["optimizer"])
        start, best = saved["epoch"] + 1, saved["best"]
        best_state, history = saved["best_state"], saved["history"]
    for epoch in range(start, epochs):
        model.train()
        total_loss, total = 0.0, 0
        loader = DataLoader(
            train_data, batch_size=batch_size, shuffle=True, generator=generator
        )
        for values, labels in loader:
            optimizer.zero_grad(set_to_none=True)
            loss = torch.nn.functional.cross_entropy(model(values), labels)
            loss.backward()
            optimizer.step()
            total_loss += float(loss.detach()) * len(labels)
            total += len(labels)
        validation_logits, validation_labels = predict(model, validation_data, batch_size)
        metrics = binary_metrics(validation_logits, validation_labels)
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
            f"epoch={epoch + 1}/{epochs} val_recall={metrics['vulnerable_recall']:.4f}",
            flush=True,
        )
    model.load_state_dict(best_state)
    torch.save(best_state, run_dir / "model.pt")
    return model, history


def run_source(args, protocol, source, seed, records_by_name, manifests):
    records = records_by_name[source]
    manifest = manifests[source]
    train_indices = list(manifest["train"])
    if protocol == "ten_percent":
        train_indices = ten_percent_indices(records, train_indices, seed)
    vocab = build_vocab(records, train_indices)
    run_dir = args.output / protocol / source / f"seed_{seed}"
    run_dir.mkdir(parents=True, exist_ok=True)
    model, history = train(
        records, train_indices, manifest["validation"], vocab, seed, args.epochs,
        args.batch_size, run_dir, args.quantum_device,
    )
    targets = [source] if protocol != "generalization" else [
        name for name in DATASETS if name != source
    ]
    for target in targets:
        target_records = records_by_name[target]
        if protocol == "generalization":
            test_indices = list(range(len(target_records)))
            scope = "full_target_dataset"
        else:
            test_indices = manifests[target]["test"]
            scope = "fixed_test_split_101"
        logits, labels = predict(
            model, Tokens(target_records, test_indices, vocab), args.batch_size
        )
        metrics = binary_metrics(logits, labels)
        payload = {
            "architecture": "RQENN",
            "protocol": protocol,
            "source": source,
            "target": target,
            "training_seed": seed,
            "split_seed": SPLIT_SEED,
            "evaluation_scope": scope,
            "train_samples": len(train_indices),
            "validation_samples": len(manifest["validation"]),
            "test_samples": len(test_indices),
            "source_manifest_sha256": manifest_hash(records, manifest),
            "paper_configuration": {
                "vocabulary": 128, "qubits": 7, "max_length": 100,
                "qembedding_layers": 4, "qweight_layers": 4,
                "parameters": 106, "epochs": args.epochs,
                "optimizer": "Adam", "learning_rate": 0.01,
            },
            "metrics": metrics,
            "history": history,
        }
        if protocol == "long_tail":
            rare = rare_cwes(records, manifest["train"])
            mask = torch.tensor([
                target_records[index]["label"] == 1
                and target_records[index]["cwe"] in rare
                for index in test_indices
            ])
            payload["long_tail"] = {
                "rare_cwes": sorted(rare),
                "rare_test_samples": int(mask.sum()),
                "rare_cwe_vulnerable_recall": (
                    float((logits[mask].argmax(-1) == 1).float().mean())
                    if mask.any() else None
                ),
            }
        name = target if protocol == "generalization" else source
        (run_dir / f"report_{name}.json").write_text(
            json.dumps(payload, indent=2) + "\n", encoding="utf-8"
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
    parser.add_argument("--epochs", type=int, default=10)
    parser.add_argument("--batch-size", type=int, default=64)
    parser.add_argument("--quantum-device", default="default.qubit")
    parser.add_argument("--cache", type=Path, default=Path("cache"))
    parser.add_argument("--output", type=Path, default=Path("results"))
    args = parser.parse_args()
    selected = DATASETS if args.dataset == "all" else (args.dataset,)
    seeds = SEEDS if args.seed is None else (args.seed,)
    records = {
        name: load_records(args.repo_root, name, args.cache) for name in DATASETS
    }
    manifests = {
        name: fixed_manifest(records[name], args.cache, name) for name in DATASETS
    }
    protocols = (
        ("in_domain", "generalization", "ten_percent", "long_tail")
        if args.protocol == "all" else (args.protocol,)
    )
    for protocol in protocols:
        for source in selected:
            for seed in seeds:
                run_source(args, protocol, source, seed, records, manifests)


if __name__ == "__main__":
    main()
