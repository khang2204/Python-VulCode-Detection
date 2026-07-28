#!/usr/bin/env python3
"""Stage existing checkpoints and submit cross-benchmark inference to Kaggle."""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import time
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
ASSETS = Path(__file__).resolve().parent / "assets"
KERNEL = Path(__file__).resolve().parent / "kernel"
RUNS = ROOT / "experiments/repeated_evaluation/runs"
DATASET = "khangtrn2/pagvul-cross-benchmark-generalization-assets"
KERNEL_ID = "khangtrn2/pag-vul-cross-benchmark-generalization"
DATASETS = ("benchmarkpython", "vudenc", "realvuln_human")
ATTENTIONS = ("classical", "quantum")
SEEDS = (101, 202, 303)


def kaggle_command() -> str:
    candidates = (ROOT / ".venv/bin/kaggle", Path(sys.executable).with_name("kaggle"))
    for candidate in candidates:
        if candidate.is_file():
            return str(candidate)
    if resolved := shutil.which("kaggle"):
        return resolved
    raise SystemExit("Kaggle CLI was not found")


def run(*args: str) -> None:
    subprocess.run(args, check=True)


def stage(runs_root: Path = RUNS) -> None:
    if ASSETS.exists():
        shutil.rmtree(ASSETS)
    ASSETS.mkdir(parents=True)
    common = (
        ROOT / "train_pagvul_binary.py",
        ROOT / "train_pagvul_classical.py",
        ROOT / "train_pagvul_quantum.py",
        ROOT / "kaggle_deploy/generalization/evaluate_cross_dataset.py",
    )
    for source in common:
        if not source.is_file():
            raise SystemExit(f"Missing required file: {source}")
        shutil.copy2(source, ASSETS / source.name)
    for dataset in DATASETS:
        for attention in ATTENTIONS:
            for seed in SEEDS:
                source = runs_root / dataset / attention / f"seed_{seed}"
                destination = ASSETS / "runs" / dataset / attention / f"seed_{seed}"
                destination.mkdir(parents=True, exist_ok=True)
                for name in ("gat_warmup_best.pt", "pagvul_binary_best.pt", "report.json"):
                    path = source / name
                    if not path.is_file():
                        raise SystemExit(f"Incomplete checkpoint: {path}")
                    shutil.copy2(path, destination / name)
    metadata = {
        "title": "PAG-Vul Cross-Benchmark Generalization Assets",
        "id": DATASET,
        "licenses": [{"name": "other"}],
    }
    (ASSETS / "dataset-metadata.json").write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")


def status(kaggle: str) -> tuple[str, int]:
    probe = subprocess.run(
        [kaggle, "datasets", "status", DATASET, "--format", "json"], capture_output=True, text=True
    )
    try:
        payload = json.loads(probe.stdout)
        return str(payload.get("status", "unknown")), int(payload.get("current_version_number", 0))
    except (json.JSONDecodeError, TypeError, ValueError):
        return "missing", 0


def wait_ready(kaggle: str, version: int) -> None:
    deadline = time.monotonic() + 600
    while time.monotonic() < deadline:
        current_status, current_version = status(kaggle)
        if current_status == "ready" and current_version >= version:
            time.sleep(20)
            return
        print(f"Waiting for checkpoint Dataset v{version}: {current_status}, current v{current_version}")
        time.sleep(10)
    raise SystemExit("Checkpoint Dataset did not become ready in 10 minutes")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--submit", action="store_true")
    parser.add_argument("--kernel-only", action="store_true")
    parser.add_argument("--accelerator", default="NvidiaTeslaT4")
    parser.add_argument(
        "--runs-root", type=Path, default=RUNS,
        help="Checkpoint tree to stage (dataset/attention/seed_<n>); defaults to the historic run tree.",
    )
    args = parser.parse_args()
    if args.submit and args.kernel_only:
        parser.error("choose only one of --submit and --kernel-only")
    if not args.kernel_only:
        stage(args.runs_root)
    print(f"Dataset: https://www.kaggle.com/datasets/{DATASET}")
    print(f"Notebook: https://www.kaggle.com/code/{KERNEL_ID}")
    if not (args.submit or args.kernel_only):
        return 0
    kaggle = kaggle_command()
    if args.submit:
        _, previous = status(kaggle)
        if previous:
            run(
                kaggle,
                "datasets",
                "version",
                "-p",
                str(ASSETS),
                "-m",
                "Update five-seed checkpoints",
                "--dir-mode",
                "zip",
            )
        else:
            run(kaggle, "datasets", "create", "-p", str(ASSETS), "--dir-mode", "zip")
        wait_ready(kaggle, previous + 1)
    run(kaggle, "kernels", "push", "-p", str(KERNEL), "--accelerator", args.accelerator)
    print("Submitted inference-only generalization run; this command does not wait for completion.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
