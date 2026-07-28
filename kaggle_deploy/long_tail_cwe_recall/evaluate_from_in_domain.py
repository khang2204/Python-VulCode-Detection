#!/usr/bin/env python3
"""Compute Long-tail CWE recall from fixed-split In-domain predictions."""
from __future__ import annotations

import argparse
import hashlib
import json
import statistics
from collections import Counter
from pathlib import Path


DATASETS = ("benchmarkpython", "vudenc", "realvuln_human")
METHODS = ("classical", "quantum")
SEEDS = (101, 202, 303)
METADATA_FILES = {
    "benchmarkpython": "BenchmarkPython/metadata.jsonl",
    "vudenc": "Vudenc/metadata.jsonl",
    "realvuln_human": "RealVulnHuman/metadata.jsonl",
}


def read_jsonl(path: Path) -> list[dict]:
    return [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def is_vulnerable(row: dict) -> bool:
    if "label" in row:
        return int(row["label"]) == 1
    value = str(row.get("real_vulnerability", "")).strip().lower()
    return value in {"1", "true", "yes"}


def canonical_manifest_hash(manifest: dict) -> str:
    value = {
        name: manifest[name]
        for name in ("train", "validation", "test")
    }
    return hashlib.sha256(
        json.dumps(value, separators=(",", ":")).encode()
    ).hexdigest()


def sample_std(values: list[float]) -> float:
    return statistics.stdev(values) if len(values) > 1 else 0.0


def evaluate(args: argparse.Namespace) -> dict:
    rows = []
    expected_hashes: dict[str, str] = {}
    for dataset in DATASETS:
        metadata_path = args.metadata_root / METADATA_FILES[dataset]
        records = {
            str(row["sample_file"]): row
            for row in read_jsonl(metadata_path)
            if row.get("sample_file")
        }
        manifest_path = (
            args.runs_root
            / dataset
            / "quantum"
            / "seed_101"
            / "split_manifest.json"
        )
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        manifest_hash = canonical_manifest_hash(manifest)
        expected_hashes[dataset] = manifest_hash
        missing = {
            sample
            for part in ("train", "validation", "test")
            for sample in manifest[part]
            if sample not in records
        }
        if missing:
            raise RuntimeError(
                f"{dataset} metadata misses manifest samples: {sorted(missing)[:5]}"
            )
        counts = Counter(
            str(records[sample].get("cwe", "UNKNOWN"))
            for sample in manifest["train"]
            if is_vulnerable(records[sample])
        )
        if not counts:
            raise RuntimeError(f"{dataset} has no vulnerable training CWE")
        cutoff = sorted(counts.values())[(len(counts) - 1) // 2]
        rare_cwes = {
            cwe for cwe, count in counts.items()
            if count <= cutoff
        }
        vulnerable_test = [
            sample for sample in manifest["test"]
            if is_vulnerable(records[sample])
        ]
        rare_test = [
            sample for sample in vulnerable_test
            if str(records[sample].get("cwe", "UNKNOWN")) in rare_cwes
        ]
        common_test = [
            sample for sample in vulnerable_test
            if str(records[sample].get("cwe", "UNKNOWN")) not in rare_cwes
        ]
        if not rare_test or not common_test:
            raise RuntimeError(
                f"{dataset} has an empty Rare/Common vulnerable test partition"
            )
        for method in METHODS:
            for seed in SEEDS:
                run_dir = args.runs_root / dataset / method / f"seed_{seed}"
                run_manifest = json.loads(
                    (run_dir / "split_manifest.json").read_text(encoding="utf-8")
                )
                if canonical_manifest_hash(run_manifest) != manifest_hash:
                    raise RuntimeError(
                        f"{dataset}/{method}/seed_{seed} manifest mismatch"
                    )
                predictions = json.loads(
                    (run_dir / "test_predictions.json").read_text(encoding="utf-8")
                )
                by_file = {
                    str(row["sample_file"]): row
                    for row in predictions
                }
                if set(by_file) != set(manifest["test"]):
                    raise RuntimeError(
                        f"{dataset}/{method}/seed_{seed} prediction identity mismatch"
                    )
                for sample in vulnerable_test:
                    if int(by_file[sample]["true_label"]) != 1:
                        raise RuntimeError(
                            f"{dataset}/{method}/seed_{seed} label mismatch: {sample}"
                        )
                rare_recall = statistics.mean(
                    int(by_file[sample]["predicted_label"]) == 1
                    for sample in rare_test
                )
                common_recall = statistics.mean(
                    int(by_file[sample]["predicted_label"]) == 1
                    for sample in common_test
                )
                rows.append(
                    {
                        "dataset": dataset,
                        "method": method,
                        "training_seed": seed,
                        "split_seed": 101,
                        "manifest_sha256": manifest_hash,
                        "rare_cwes": sorted(rare_cwes),
                        "rare_test_samples": len(rare_test),
                        "common_test_samples": len(common_test),
                        "rare_cwe_vulnerable_recall": rare_recall,
                        "common_cwe_vulnerable_recall": common_recall,
                        "source_predictions": str(
                            run_dir / "test_predictions.json"
                        ),
                    }
                )
    summary = {}
    for dataset in DATASETS:
        summary[dataset] = {}
        for method in METHODS:
            selected = [
                row for row in rows
                if row["dataset"] == dataset and row["method"] == method
            ]
            rare = [
                row["rare_cwe_vulnerable_recall"]
                for row in selected
            ]
            common = [
                row["common_cwe_vulnerable_recall"]
                for row in selected
            ]
            summary[dataset][method] = {
                "rare_cwe_vulnerable_recall": {
                    "mean": statistics.mean(rare),
                    "sample_std": sample_std(rare),
                },
                "common_cwe_vulnerable_recall": {
                    "mean": statistics.mean(common),
                    "sample_std": sample_std(common),
                },
                "rare_test_samples": selected[0]["rare_test_samples"],
                "common_test_samples": selected[0]["common_test_samples"],
            }
    return {
        "protocol": {
            "scenario": "long_tail_cwe_recall",
            "split_seed": 101,
            "model_source": "fixed-split In-domain checkpoints/predictions",
            "retraining": False,
            "decision_threshold": 0.5,
            "rare_definition": (
                "training CWE frequency <= lower median training CWE frequency"
            ),
            "manifest_sha256": expected_hashes,
        },
        "runs": rows,
        "summary": summary,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--runs-root", type=Path, required=True)
    parser.add_argument(
        "--metadata-root",
        type=Path,
        default=Path(__file__).resolve().parents[2] / "CPG",
    )
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    payload = evaluate(args)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload["summary"], indent=2))


if __name__ == "__main__":
    main()
