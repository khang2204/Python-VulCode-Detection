#!/usr/bin/env python3
"""Deploy the standalone VUDENC PAG-Vul experiment to Kaggle."""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import time
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
ASSETS = Path(__file__).resolve().parent / "assets"
KERNEL = Path(__file__).resolve().parent / "kernel"
DATASET = "khangtrn2/vudenc-pagvul-binary-assets"
KERNEL_ID = "khangtrn2/vudenc-pag-vul-binary-training"
ARTIFACT_DIR = ROOT / "artifacts" / "vudenc_binary_pyg"
GRAPH = ARTIFACT_DIR / "vudenc_binary_graphs.pt"
PREPARE_REPORT = ROOT / "CPG" / "Vudenc" / "prepare_report.json"
EXPORT_REPORT = ARTIFACT_DIR / "report.json"
COMMON_FILES = (
    (ROOT / "train_pagvul_binary.py", "train_pagvul_binary.py"),
    (ROOT / "train_pagvul_classical.py", "train_pagvul_classical.py"),
    (ROOT / "train_pagvul_quantum.py", "train_pagvul_quantum.py"),
)


def kaggle_command() -> str:
    for candidate in (ROOT / ".venv" / "bin" / "kaggle", Path(sys.executable).with_name("kaggle")):
        if candidate.is_file():
            return str(candidate)
    if resolved := shutil.which("kaggle"):
        return resolved
    raise SystemExit("Kaggle CLI was not found. Install it with: .venv/bin/pip install kaggle")


def run(*args: str) -> None:
    subprocess.run(args, check=True)


def dataset_exists(kaggle: str) -> bool:
    return subprocess.run([kaggle, "datasets", "status", DATASET], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode == 0


def dataset_version_number(kaggle: str) -> int:
    probe = subprocess.run([kaggle, "datasets", "status", DATASET, "--format", "json"], capture_output=True, text=True)
    try:
        return int(json.loads(probe.stdout).get("current_version_number", 0))
    except (json.JSONDecodeError, TypeError, ValueError):
        return 0


def wait_for_dataset_ready(kaggle: str, expected_version: int, timeout_seconds: int = 600) -> None:
    deadline = time.monotonic() + timeout_seconds
    while True:
        probe = subprocess.run([kaggle, "datasets", "status", DATASET, "--format", "json"], capture_output=True, text=True)
        try:
            payload = json.loads(probe.stdout)
            status = payload.get("status", "unknown")
            current_version = int(payload.get("current_version_number", 0))
        except (json.JSONDecodeError, TypeError, ValueError):
            status = "unknown"
            current_version = 0
        if status == "ready" and current_version >= expected_version:
            print(f"Dataset version {current_version} is ready; pushing notebook.")
            return
        if time.monotonic() >= deadline:
            raise SystemExit(f"Dataset did not become ready within {timeout_seconds}s (last status: {status!r}).")
        print(f"Waiting for Dataset version {expected_version} (current: {current_version}, status: {status!r})...")
        time.sleep(10)


def stage_assets(attention: str, seed: int, split_seed: int) -> None:
    files = (
        (GRAPH, "vudenc_binary_graphs.pt"),
        (PREPARE_REPORT, "prepare_report.json"),
        (EXPORT_REPORT, "export_report.json"),
        *COMMON_FILES,
    )
    missing = [path for path, _ in files if not path.is_file()]
    if missing:
        raise SystemExit("Missing required asset(s): " + ", ".join(map(str, missing)))
    ASSETS.mkdir(parents=True, exist_ok=True)
    for path, asset_name in files:
        shutil.copy2(path, ASSETS / asset_name)
    config = {
        "attention": attention,
        "representation": "vudenc_raw_statement_context_blocks_joern_only",
        "corpus_selection": "all_labelled_blocks; Joern graph construction is the only parser gate",
        "split_mode": "standard",
        "output_prefix": "vudenc_binary",
        "trainer_args": {"seed": seed, "split_seed": split_seed, "attention_dim": 64, "value_dim": 64, "head_learning_rate": 0.002},
    }
    if attention == "quantum":
        config["trainer_args"].update({"n_qubits": 10, "quantum_depth": 5})
    (ASSETS / "run_config.json").write_text(json.dumps(config, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--attention", choices=("classical", "quantum"), default="classical")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--split-seed", type=int, default=42)
    parser.add_argument("--message", default="Update VUDENC PAG-Vul binary assets")
    parser.add_argument("--accelerator", default="NvidiaTeslaT4")
    parser.add_argument("--submit", action="store_true")
    parser.add_argument("--kernel-only", action="store_true")
    args = parser.parse_args()
    if args.submit and args.kernel_only:
        parser.error("--submit and --kernel-only cannot be used together")
    if not args.kernel_only:
        stage_assets(args.attention, args.seed, args.split_seed)
    print(f"Dataset: https://www.kaggle.com/datasets/{DATASET}")
    print(f"Notebook: https://www.kaggle.com/code/{KERNEL_ID}")
    if not args.submit and not args.kernel_only:
        return 0
    kaggle = kaggle_command()
    if args.submit:
        previous_version = dataset_version_number(kaggle) if dataset_exists(kaggle) else 0
        if previous_version:
            run(kaggle, "datasets", "version", "-p", str(ASSETS), "-m", args.message)
        else:
            run(kaggle, "datasets", "create", "-p", str(ASSETS))
        wait_for_dataset_ready(kaggle, expected_version=previous_version + 1)
    run(kaggle, "kernels", "push", "-p", str(KERNEL), "--accelerator", args.accelerator)
    print("Submitted to Kaggle; this command intentionally does not wait for completion.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
