#!/usr/bin/env python3
"""Run HQCDNN on all four fixed-split benchmark protocols."""
from __future__ import annotations

import argparse
import json
import math
from collections import Counter
from pathlib import Path

import torch
from torch.utils.data import DataLoader, Dataset

from common import (
    DATASETS, SEEDS, SPLIT_SEED, binary_metrics, fixed_manifest, load_records,
    manifest_hash, rare_cwes, set_seed, ten_percent_indices,
)
from model import HQCDNN


class BigramTfidf:
    """Train-only TF-IDF over normalized token bigrams."""

    def __init__(self, max_features: int = 512):
        self.max_features = max_features
        self.vocabulary: dict[str, int] = {}
        self.idf = torch.empty(0)

    @staticmethod
    def terms(record):
        values = record["tokens"]
        return [f"{left}\u241f{right}" for left, right in zip(values, values[1:])]

    def fit(self, records, indices):
        document_frequency = Counter()
        term_frequency = Counter()
        for index in indices:
            terms = self.terms(records[index])
            term_frequency.update(terms)
            document_frequency.update(set(terms))
        selected = [
            term for term, _ in term_frequency.most_common(self.max_features)
        ]
        self.vocabulary = {term: index for index, term in enumerate(selected)}
        n_documents = len(indices)
        self.idf = torch.tensor([
            math.log((1 + n_documents) / (1 + document_frequency[term])) + 1
            for term in selected
        ], dtype=torch.float32)
        return self

    def transform_one(self, record):
        counts = Counter(self.terms(record))
        output = torch.zeros(len(self.vocabulary), dtype=torch.float32)
        total = max(1, sum(counts.values()))
        for term, count in counts.items():
            if term in self.vocabulary:
                offset = self.vocabulary[term]
                output[offset] = count / total * self.idf[offset]
        norm = output.norm()
        return output / norm if norm else output


class Features(Dataset):
    def __init__(self, records, indices, vectorizer):
        self.records, self.indices, self.vectorizer = records, indices, vectorizer

    def __len__(self):
        return len(self.indices)

    def __getitem__(self, offset):
        record = self.records[self.indices[offset]]
        return self.vectorizer.transform_one(record), torch.tensor(record["label"])


@torch.no_grad()
def predict(model, dataset, batch_size):
    model.eval()
    logits, labels = [], []
    for values, targets in DataLoader(dataset, batch_size=batch_size):
        logits.append(model(values).cpu())
        labels.append(targets.cpu())
    return torch.cat(logits), torch.cat(labels)


def fit_model(args, records, train_indices, validation_indices, seed, run_dir):
    vectorizer = BigramTfidf(args.max_features).fit(records, train_indices)
    set_seed(seed)
    model = HQCDNN(
        input_dim=len(vectorizer.vocabulary),
        qubits=args.qubits,
        quantum_layers=args.quantum_layers,
        quantum_device=args.quantum_device,
    )
    optimizer = torch.optim.Adam(model.parameters(), lr=args.learning_rate)
    train_data = Features(records, train_indices, vectorizer)
    validation_data = Features(records, validation_indices, vectorizer)
    generator = torch.Generator().manual_seed(seed)
    checkpoint = run_dir / "checkpoint.pt"
    start, best, best_state, history = 0, -1.0, None, []
    if checkpoint.is_file():
        saved = torch.load(checkpoint, map_location="cpu", weights_only=False)
        model.load_state_dict(saved["model"])
        optimizer.load_state_dict(saved["optimizer"])
        start, best = saved["epoch"] + 1, saved["best"]
        best_state, history = saved["best_state"], saved["history"]
    stale = 0
    for epoch in range(start, args.epochs):
        model.train()
        total_loss, total = 0.0, 0
        loader = DataLoader(
            train_data, batch_size=args.batch_size, shuffle=True, generator=generator
        )
        for values, labels in loader:
            optimizer.zero_grad(set_to_none=True)
            loss = torch.nn.functional.cross_entropy(model(values), labels)
            loss.backward()
            optimizer.step()
            total_loss += float(loss.detach()) * len(labels)
            total += len(labels)
        logits, labels = predict(model, validation_data, args.batch_size)
        metrics = binary_metrics(logits, labels)
        if metrics["vulnerable_recall"] > best:
            best = metrics["vulnerable_recall"]
            stale = 0
            best_state = {
                name: value.detach().cpu().clone()
                for name, value in model.state_dict().items()
            }
        else:
            stale += 1
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
            f"epoch={epoch + 1}/{args.epochs} val_recall={metrics['vulnerable_recall']:.4f}",
            flush=True,
        )
        if args.patience and stale >= args.patience:
            break
    model.load_state_dict(best_state)
    torch.save(best_state, run_dir / "model.pt")
    torch.save({
        "vocabulary": vectorizer.vocabulary,
        "idf": vectorizer.idf,
        "max_features": vectorizer.max_features,
    }, run_dir / "tfidf.pt")
    return model, vectorizer, history


def load_pretrained_model(args, source, seed):
    if args.pretrained_in_domain is None:
        return None
    directory = (
        args.pretrained_in_domain
        / f"{args.qubits}q"
        / source
        / f"seed_{seed}"
    )
    model_path = directory / "model.pt"
    tfidf_path = directory / "tfidf.pt"
    if not model_path.is_file() or not tfidf_path.is_file():
        raise FileNotFoundError(
            f"Missing pretrained HQCDNN in-domain artifacts under {directory}"
        )
    saved = torch.load(tfidf_path, map_location="cpu", weights_only=False)
    vectorizer = BigramTfidf(saved["max_features"])
    vectorizer.vocabulary = saved["vocabulary"]
    vectorizer.idf = saved["idf"]
    model = HQCDNN(
        input_dim=len(vectorizer.vocabulary),
        qubits=args.qubits,
        quantum_layers=args.quantum_layers,
        quantum_device=args.quantum_device,
    )
    model.load_state_dict(
        torch.load(model_path, map_location="cpu", weights_only=True)
    )
    print(
        f"REUSE HQCDNN {args.qubits}q source={source} seed={seed}",
        flush=True,
    )
    return model, vectorizer, []


def run_source(args, protocol, source, seed, records_by_name, manifests):
    source_records = records_by_name[source]
    manifest = manifests[source]
    train_indices = list(manifest["train"])
    if protocol == "ten_percent":
        train_indices = ten_percent_indices(source_records, train_indices, seed)
    run_dir = (
        args.output / f"{args.qubits}q" / protocol / source / f"seed_{seed}"
    )
    run_dir.mkdir(parents=True, exist_ok=True)
    reused = (
        load_pretrained_model(args, source, seed)
        if protocol in {"generalization", "long_tail"}
        else None
    )
    if reused is None:
        model, vectorizer, history = fit_model(
            args, source_records, train_indices, manifest["validation"], seed, run_dir
        )
    else:
        model, vectorizer, history = reused
    targets = [source] if protocol != "generalization" else [
        name for name in DATASETS if name != source
    ]
    for target in targets:
        target_records = records_by_name[target]
        if protocol == "generalization":
            indices = list(range(len(target_records)))
            scope = "full_target_dataset"
        else:
            indices = manifests[target]["test"]
            scope = "fixed_test_split_101"
        logits, labels = predict(
            model, Features(target_records, indices, vectorizer), args.batch_size
        )
        payload = {
            "architecture": "HQCDNN",
            "protocol": protocol,
            "source": source,
            "target": target,
            "training_seed": seed,
            "split_seed": SPLIT_SEED,
            "evaluation_scope": scope,
            "train_samples": len(train_indices),
            "validation_samples": len(manifest["validation"]),
            "test_samples": len(indices),
            "source_manifest_sha256": manifest_hash(source_records, manifest),
            "configuration": {
                "qubits": args.qubits,
                "quantum_layers": args.quantum_layers,
                "tfidf": "normalized Python token bigrams",
                "tfidf_max_features": args.max_features,
                "epochs": args.epochs,
                "batch_size": args.batch_size,
                "optimizer": "Adam",
                "learning_rate": args.learning_rate,
                "adaptation_note": (
                    "The paper uses EVM opcode bigrams. Python lexical-token "
                    "bigrams are the declared cross-language adaptation."
                ),
                "reused_fixed_split_in_domain_model": reused is not None,
            },
            "metrics": binary_metrics(logits, labels),
            "history": history,
        }
        if protocol == "long_tail":
            rare = rare_cwes(source_records, manifest["train"])
            mask = torch.tensor([
                target_records[index]["label"] == 1
                and target_records[index]["cwe"] in rare for index in indices
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
    parser.add_argument("--qubits", type=int, choices=(2, 4), default=4)
    parser.add_argument("--quantum-layers", type=int, default=1)
    parser.add_argument("--quantum-device", default="default.qubit")
    parser.add_argument("--max-features", type=int, default=512)
    parser.add_argument("--epochs", type=int, default=50)
    parser.add_argument("--batch-size", type=int, default=64)
    parser.add_argument("--learning-rate", type=float, default=0.005)
    parser.add_argument("--patience", type=int, default=10)
    parser.add_argument("--cache", type=Path, default=Path("cache"))
    parser.add_argument("--output", type=Path, default=Path("results"))
    parser.add_argument(
        "--pretrained-in-domain",
        type=Path,
        help=(
            "Root containing <qubits>q/<dataset>/seed_<seed>/{model,tfidf}.pt; "
            "used by generalization and long-tail without retraining."
        ),
    )
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
