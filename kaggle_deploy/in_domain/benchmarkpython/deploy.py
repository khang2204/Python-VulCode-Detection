#!/usr/bin/env python3
"""Version BenchmarkPython assets and submit a Kaggle notebook, then exit.

The script deliberately does not poll a submitted run.  Open the printed URL
in Kaggle to follow the session; invoke it again only after changing code or
after Codex has applied a fix.
"""

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
DATASET = "khangtrn2/benchmarkpython-pagvul-binary-assets"
KERNEL_ID = "khangtrn2/benchmarkpython-pag-vul-binary-training"
KAGGLE_CANDIDATES = (
    ROOT / ".venv" / "bin" / "kaggle",
    Path(sys.executable).with_name("kaggle"),
)
ASSET_FILES = (
    ROOT / "artifacts" / "benchmarkpython_binary_pyg" / "benchmarkpython_binary_graphs.pt",
    ROOT / "train_pagvul_binary.py",
    ROOT / "train_pagvul_classical.py",
    ROOT / "train_pagvul_quantum.py",
)


def run(*args: str) -> None:
    subprocess.run(args, check=True)


def kaggle_command() -> str:
    for candidate in KAGGLE_CANDIDATES:
        if candidate.is_file():
            return str(candidate)
    resolved = shutil.which("kaggle")
    if resolved:
        return resolved
    raise SystemExit(
        "Kaggle CLI was not found. Install it in .venv with: .venv/bin/pip install kaggle"
    )


def stage_assets(attention: str, seed: int, split_seed: int) -> None:
    missing = [path for path in ASSET_FILES if not path.is_file()]
    if missing:
        raise SystemExit("Missing required asset(s): " + ", ".join(map(str, missing)))
    for path in ASSET_FILES:
        shutil.copy2(path, ASSETS / path.name)
    config = {
        "attention": attention,
        "trainer_args": {"seed": seed, "split_seed": split_seed, "attention_dim": 64, "value_dim": 64, "head_learning_rate": 0.002},
    }
    if attention == "quantum":
        config["trainer_args"].update({"n_qubits": 10, "quantum_depth": 5})
    (ASSETS / "run_config.json").write_text(json.dumps(config, indent=2) + "\n", encoding="utf-8")


def dataset_exists(kaggle: str) -> bool:
    probe = subprocess.run(
        [kaggle, "datasets", "status", DATASET], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
    )
    return probe.returncode == 0


def wait_for_dataset_ready(kaggle: str, timeout_seconds: int = 600) -> None:
    """Do not push the notebook while Kaggle is still indexing a Dataset version."""
    deadline = time.monotonic() + timeout_seconds
    while True:
        probe = subprocess.run(
            [kaggle, "datasets", "status", DATASET, "--format", "json"],
            check=False,
            capture_output=True,
            text=True,
        )
        try:
            status = json.loads(probe.stdout).get("status", "unknown")
        except json.JSONDecodeError:
            status = "unknown"
        if status == "ready":
            print("Dataset version is ready; pushing notebook.")
            return
        if time.monotonic() >= deadline:
            raise SystemExit(f"Dataset did not become ready within {timeout_seconds}s (last status: {status!r}).")
        print(f"Waiting for Dataset version to become ready (current status: {status!r})...")
        time.sleep(10)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--attention", choices=("classical", "quantum"), default="classical")
    parser.add_argument("--seed", type=int, default=42, help="Training random seed.")
    parser.add_argument("--split-seed", type=int, default=42, help="Fixed data-split seed.")
    parser.add_argument("--message", default="Update BenchmarkPython PAG-Vul binary assets")
    parser.add_argument(
        "--accelerator",
        default="NvidiaTeslaT4",
        help="Kaggle accelerator requested for the run (default: NvidiaTeslaT4).",
    )
    parser.add_argument("--submit", action="store_true", help="Upload a Dataset version and push/run the Kaggle notebook.")
    parser.add_argument(
        "--kernel-only",
        action="store_true",
        help="Push/run only notebook code; use only when its input Dataset is already current.",
    )
    args = parser.parse_args()
    if args.submit and args.kernel_only:
        parser.error("--submit and --kernel-only cannot be used together")
    if not args.kernel_only:
        stage_assets(args.attention, args.seed, args.split_seed)
        print(f"Staged assets for {args.attention} attention.")
    print(f"Dataset: https://www.kaggle.com/datasets/{DATASET}")
    print(f"Notebook: https://www.kaggle.com/code/{KERNEL_ID}")
    if not args.submit and not args.kernel_only:
        print("Dry preparation only. Re-run with --submit to upload and start Kaggle Run All.")
        return 0
    kaggle = kaggle_command()
    if args.submit:
        if dataset_exists(kaggle):
            run(kaggle, "datasets", "version", "-p", str(ASSETS), "-m", args.message)
        else:
            run(kaggle, "datasets", "create", "-p", str(ASSETS))
        wait_for_dataset_ready(kaggle)
    run(kaggle, "kernels", "push", "-p", str(KERNEL), "--accelerator", args.accelerator)
    print("Submitted to Kaggle; this command intentionally does not wait for completion.")
    print(f"Follow the run at: https://www.kaggle.com/code/{KERNEL_ID}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
