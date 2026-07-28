#!/usr/bin/env python3
"""Controlled label-efficiency comparison for original PAG-Vul heads.

The validation and test partitions are fixed from the original repeated-
evaluation manifest.  Only the training partition is subsampled.  Classical
and Quantum heads receive the identical warm-start encoder, embeddings,
prototypes, and sampled graph list at each data budget.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from collections import Counter
from dataclasses import replace
from pathlib import Path
from statistics import mean

import torch
from torch_geometric.loader import DataLoader

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from train_pagvul_binary import BinaryPAG, Config, build_binary_prototypes, evaluate, train_head
from train_pagvul_quantum import GATWarmup, GraphEncoder, class_weights, extract_embeddings, parse_device, set_seed, train_classifier


DATASETS = ("benchmarkpython", "vudenc", "realvuln_human")


def load_manifest(path: Path) -> dict[str, list[str]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not {"train", "validation", "test"}.issubset(payload):
        raise RuntimeError(f"Incomplete split manifest: {path}")
    return {name: [str(value) for value in payload[name]] for name in ("train", "validation", "test")}


def split_from_manifest(graphs: list, manifest: dict[str, list[str]]) -> dict[str, list]:
    table = {str(graph.sample_file): graph for graph in graphs}
    wanted = {sample for values in manifest.values() for sample in values}
    missing = wanted - set(table)
    if missing:
        raise RuntimeError(f"Manifest references unknown samples: {sorted(missing)[:5]}")
    if any(set(manifest[left]) & set(manifest[right]) for left, right in (("train", "validation"), ("train", "test"), ("validation", "test"))):
        raise RuntimeError("Manifest contains split leakage")
    return {name: [table[sample] for sample in manifest[name]] for name in manifest}


def sample_train(graphs: list, fraction: float, seed: int) -> list:
    """Sample each binary/CWE stratum so rare vulnerabilities remain represented."""
    groups: dict[tuple[int, str], list] = {}
    for graph in graphs:
        label = int(graph.y.item())
        key = (label, "BENIGN" if label == 0 else str(graph.cwe))
        groups.setdefault(key, []).append(graph)
    generator = torch.Generator().manual_seed(seed)
    chosen = []
    for key in sorted(groups):
        members = sorted(groups[key], key=lambda graph: str(graph.sample_file))
        amount = min(len(members), max(1, round(len(members) * fraction)))
        order = torch.randperm(len(members), generator=generator)[:amount].tolist()
        chosen.extend(members[index] for index in order)
    return sorted(chosen, key=lambda graph: str(graph.sample_file))


def binary_counts(graphs: list) -> dict[str, int]:
    counts = Counter(int(graph.y.item()) for graph in graphs)
    return {"benign": counts[0], "vulnerable": counts[1], "total": len(graphs)}


def long_tail_partition(split: dict[str, list]) -> dict:
    """Derive Rare/Common vulnerable test sets from this exact fixed split."""
    counts = Counter(
        str(graph.cwe) for graph in split["train"] if int(graph.y.item()) == 1
    )
    if not counts:
        raise RuntimeError("Cannot derive Long-tail CWEs: training split has no vulnerable samples")
    cutoff = sorted(counts.values())[(len(counts) - 1) // 2]
    rare_cwes = {cwe for cwe, count in counts.items() if count <= cutoff}
    vulnerable_test = [graph for graph in split["test"] if int(graph.y.item()) == 1]
    rare_test_files = [str(graph.sample_file) for graph in vulnerable_test if str(graph.cwe) in rare_cwes]
    common_test_files = [str(graph.sample_file) for graph in vulnerable_test if str(graph.cwe) not in rare_cwes]
    if len(rare_test_files) + len(common_test_files) != len(vulnerable_test):
        raise RuntimeError("Long-tail partition does not cover every vulnerable test sample")
    return {
        "rare_cwes": sorted(rare_cwes),
        "rare_test_files": rare_test_files,
        "common_test_files": common_test_files,
    }

def auc(labels: list[int], scores: list[float]) -> float:
    positives=sum(labels); negatives=len(labels)-positives
    if not positives or not negatives: return float('nan')
    order=sorted(range(len(scores)),key=lambda i:scores[i]); ranks=[0.0]*len(scores); index=0
    while index<len(order):
        end=index
        while end+1<len(order) and scores[order[end+1]]==scores[order[index]]: end+=1
        rank=(index+end+2)/2
        for j in range(index,end+1): ranks[order[j]]=rank
        index=end+1
    return (sum(rank for rank,label in zip(ranks,labels) if label)-positives*(positives+1)/2)/(positives*negatives)


def run_budget(
    dataset: str,
    split: dict[str, list],
    base_config: Config,
    fraction: float,
    sampling_seed: int,
    training_seed: int,
    device: torch.device,
    work_dir: Path,
    quantum_head_learning_rate: float | None,
) -> dict:
    train_graphs = sample_train(split["train"], fraction, sampling_seed)
    run_seed = training_seed
    run_config = replace(base_config, seed=run_seed)
    set_seed(run_seed)
    weights = class_weights(train_graphs, 2, device)
    encoder = GraphEncoder(
        int(train_graphs[0].x.size(1)), run_config.hidden_dim, run_config.embedding_dim,
        run_config.gat_layers, run_config.gat_heads, run_config.dropout,
    )
    warmup = GATWarmup(encoder, 2).to(device)
    warmup_dir = work_dir / "warmup"
    warmup_dir.mkdir(parents=True, exist_ok=True)
    checkpoint_path = warmup_dir / "gat_warmup_best.pt"
    warmup_history = train_classifier(
        warmup,
        DataLoader(train_graphs, batch_size=run_config.batch_size, shuffle=True),
        DataLoader(split["validation"], batch_size=run_config.batch_size, shuffle=False),
        2, device, run_config.warmup_epochs, run_config.learning_rate,
        run_config.weight_decay, weights, checkpoint_path,
    )
    for parameter in warmup.encoder.parameters():
        parameter.requires_grad_(False)
    warmup.encoder.eval()
    q_train, y_train, _ = extract_embeddings(warmup.encoder, train_graphs, run_config.batch_size, device)
    q_val, y_val, _ = extract_embeddings(warmup.encoder, split["validation"], run_config.batch_size, device)
    q_test, y_test, test_files = extract_embeddings(warmup.encoder, split["test"], run_config.batch_size, device)
    checkpoint_path.unlink(missing_ok=True)
    prototypes, prototype_manifest = build_binary_prototypes(
        q_train, y_train, [str(graph.cwe) for graph in train_graphs],
        run_config.top_cwes, run_config.prototypes_per_cwe, run_config.benign_prototypes, run_seed,
    )
    outcomes = {}
    for attention in ("classical", "quantum"):
        set_seed(run_seed)
        config = replace(
            run_config,
            attention=attention,
            head_learning_rate=(quantum_head_learning_rate if attention == "quantum" and quantum_head_learning_rate is not None else run_config.head_learning_rate),
        )
        model = BinaryPAG(config, prototypes.to(device)).to(device)
        model, history = train_head(model, q_train, y_train, q_val, y_val, weights, config, device)
        model.eval()
        with torch.no_grad(): logits,_=model(q_test.to(device)); probabilities=torch.softmax(logits,dim=-1).cpu()
        outcomes[attention] = {
            "test": evaluate(model, q_test, y_test, device),
            "best_validation": max(history, key=lambda row: (float(row["f1"]), float(row["balanced_accuracy"]))),
            "trainable_head_parameters": sum(parameter.numel() for parameter in model.parameters()),
            "test_predictions": [{"sample_file":str(file),"label":int(label),"vulnerable_probability":float(prob[1]),"confidence":float(prob.max())} for file,label,prob in zip(test_files,y_test.tolist(),probabilities)],
        }
    sampled_train_files = [str(graph.sample_file) for graph in train_graphs]
    return {
        "dataset": dataset,
        "fraction": fraction,
        "sampling_seed": sampling_seed,
        "training_seed": training_seed,
        "fixed_split_sizes": {name: len(values) for name, values in split.items()},
        "sampled_train_counts": binary_counts(train_graphs),
        "sampled_train_files": sampled_train_files,
        "sampled_train_sha256": hashlib.sha256(
            json.dumps(sampled_train_files, separators=(",", ":")).encode()
        ).hexdigest(),
        "prototype_manifest": prototype_manifest,
        "warmup_last": warmup_history[-1],
        "outcomes": outcomes,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--assets", type=Path, required=True)
    parser.add_argument("--manifest-root", type=Path, help="Optional separate root holding split manifests.")
    parser.add_argument("--open-set-metadata", type=Path, help="Per-seed unknown CWE metadata for open-set metrics.")
    parser.add_argument("--long-tail-metadata", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--split-seed", type=int, default=101, help="Original fixed split manifest to reuse.")
    parser.add_argument("--fractions", type=float, nargs="+", default=[0.1, 0.2, 0.4, 0.7, 1.0])
    parser.add_argument("--sampling-seed", type=int, default=101)
    parser.add_argument("--training-seed", type=int,
                        help="Training randomness seed; defaults to --sampling-seed for compatibility.")
    parser.add_argument("--datasets", nargs="+", choices=DATASETS, default=DATASETS,
                        help="Benchmarks to evaluate; defaults to all three.")
    parser.add_argument("--quantum-head-learning-rate", type=float, default=None,
                        help="Optional Quantum-head-only learning rate; Classical remains unchanged.")
    parser.add_argument("--device", default="cuda")
    args = parser.parse_args()
    if any(not 0 < fraction <= 1 for fraction in args.fractions):
        parser.error("Every --fractions value must be in (0, 1].")
    device = parse_device(args.device)
    training_seed = args.training_seed if args.training_seed is not None else args.sampling_seed
    manifest_root = args.manifest_root or args.assets
    torch.set_float32_matmul_precision("high")
    runs = []
    long_tail_by_dataset = {}
    for dataset in args.datasets:
        graphs = torch.load(args.assets / f"{dataset}_binary_graphs.pt", map_location="cpu", weights_only=False)
        manifest = load_manifest(manifest_root / f"{dataset}_seed_{args.split_seed}_split_manifest.json")
        split = split_from_manifest(graphs, manifest)
        if args.long_tail_metadata:
            long_tail_by_dataset[dataset] = long_tail_partition(split)
        config_data = json.loads((args.assets / f"{dataset}_config.json").read_text(encoding="utf-8"))
        base_config = Config(**config_data)
        for fraction in args.fractions:
            budget_seed = args.sampling_seed
            print(f"Running {dataset} fraction={fraction:.2f}", flush=True)
            runs.append(run_budget(dataset, split, base_config, fraction, budget_seed, training_seed, device, args.output.parent / "work" / dataset / f"fraction_{fraction:.2f}", args.quantum_head_learning_rate))
    if args.open_set_metadata:
        metadata=json.loads(args.open_set_metadata.read_text(encoding='utf-8'))
        for row in runs:
            unknown=set(metadata[row['dataset']]['unknown_test_files'])
            for result in row['outcomes'].values():
                vulnerable=[item for item in result['test_predictions'] if item['label']==1]
                labels=[int(item['sample_file'] in unknown) for item in vulnerable]
                scores=[1-item['confidence'] for item in vulnerable]
                known=[item['confidence'] for item,label in zip(vulnerable,labels) if not label]; unseen=[item['confidence'] for item,label in zip(vulnerable,labels) if label]
                result['open_set']={'unknown_detection_auroc':auc(labels,scores),'known_confidence_mean':mean(known),'unknown_confidence_mean':mean(unseen),'confidence_gap_known_minus_unknown':mean(known)-mean(unseen),'known_count':len(known),'unknown_count':len(unseen)}
    if args.long_tail_metadata:
        for row in runs:
            tail=long_tail_by_dataset[row['dataset']]
            for result in row['outcomes'].values():
                predictions={item['sample_file']:int(item['vulnerable_probability']>=.5) for item in result['test_predictions']}
                expected=tail['rare_test_files'] + tail['common_test_files']
                missing=[sample for sample in expected if sample not in predictions]
                if missing:
                    raise RuntimeError(f"Long-tail metadata/prediction mismatch for {row['dataset']}: {missing[:5]}")
                rare=[predictions[x] for x in tail['rare_test_files']]; common=[predictions[x] for x in tail['common_test_files']]
                result['long_tail']={'rare_cwe_recall':sum(rare)/len(rare),'common_cwe_recall':sum(common)/len(common),'rare_test_count':len(rare),'common_test_count':len(common),'rare_cwes':tail['rare_cwes']}
    summary = {}
    for dataset in args.datasets:
        summary[dataset] = {}
        for fraction in args.fractions:
            matching = [row for row in runs if row["dataset"] == dataset and row["fraction"] == fraction]
            summary[dataset][str(fraction)] = {
                attention: {
                    metric: mean(row["outcomes"][attention]["test"][metric] for row in matching)
                    for metric in ("accuracy", "balanced_accuracy", "precision", "recall", "f1")
                }
                for attention in ("classical", "quantum")
            }
    payload = {
        "protocol": {
            "scenario": "sample efficiency / label-efficient vulnerability detection",
            "fixed_split_seed": args.split_seed,
            "sampling_seed": args.sampling_seed,
            "training_seed": training_seed,
            "fractions": args.fractions,
            "test_and_validation": "fixed original partitions; never subsampled",
            "fairness": "classical and quantum share sampled train graphs, warm-start GAT encoder, embeddings, and prototypes per budget",
            "quantum_configuration": f"PAG-Vul Quantum head: {base_config.n_qubits} qubits, depth {base_config.quantum_depth}",
        },
        "runs": runs,
        "summary": summary,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(json.dumps(summary, indent=2), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
