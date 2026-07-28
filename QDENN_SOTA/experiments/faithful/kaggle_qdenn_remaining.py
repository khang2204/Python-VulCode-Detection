#!/usr/bin/env python3
"""Stage and submit one CPU notebook for remaining QDENN protocols."""
from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parents[2]
STAGE = HERE / "kaggle_remaining"
ASSETS = STAGE / "assets"
KERNEL = STAGE / "kernel"
ACCOUNT = "ryhvic"
REMAINING_ASSET_REF = f"{ACCOUNT}/qdenn-remaining-fixedsplit101-assets"
TEN_PERCENT_ASSET_REF = (
    f"{ACCOUNT}/qdenn-ten-percent-fixed-sampling-101-assets"
)
REMAINING_KERNEL_REF = f"{ACCOUNT}/qdenn-remaining-fixed-split-101"
TEN_PERCENT_KERNEL_REF = (
    f"{ACCOUNT}/qdenn-ten-percent-fixed-sampling-101"
)
DATASETS = ("benchmarkpython", "vudenc", "realvuln_human")
SEEDS = (101, 202, 303)


def command_env():
    token = os.environ.get("KAGGLE_API_TOKEN")
    if not token:
        raise SystemExit("KAGGLE_API_TOKEN is required")
    return {**os.environ, "KAGGLE_API_TOKEN": token}


def kaggle(*arguments, capture=False):
    return subprocess.run(
        [sys.executable, "-m", "kaggle", *arguments],
        check=True,
        text=True,
        capture_output=capture,
        env=command_env(),
    )


def verify_account():
    from kaggle.api.kaggle_api_extended import KaggleApi

    api = KaggleApi()
    api.authenticate()
    actual = api.config_values.get("username")
    if actual != ACCOUNT:
        raise RuntimeError(f"Expected {ACCOUNT}, authenticated as {actual}")


def stage_assets(asset_ref: str):
    sys.path.insert(0, str(HERE))
    from data import prepare_dataset

    cache = ASSETS / "cache"
    cache.mkdir(parents=True, exist_ok=True)
    for dataset in DATASETS:
        prepare_dataset(REPO_ROOT, dataset, cache, 101)
    for name in ("data.py", "models.py", "run_remaining.py", "FIDELITY.md"):
        shutil.copy2(HERE / name, ASSETS / name)

    source_root = (
        REPO_ROOT
        / "QDENN_SOTA"
        / "experiments"
        / "results"
        / "qdenn_faithful_indomain_fixedsplit101"
    )
    destination = ASSETS / "in_domain_models"
    if destination.exists():
        shutil.rmtree(destination)
    for dataset in DATASETS:
        for seed in SEEDS:
            source = (
                source_root
                / dataset
                / "results"
                / "qdenn"
                / dataset
                / f"seed_{seed}"
                / "model.pt"
            )
            if not source.is_file():
                raise FileNotFoundError(source)
            target = destination / dataset / f"seed_{seed}" / "model.pt"
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)
    metadata = {
        "title": asset_ref.partition("/")[2],
        "id": asset_ref,
        "licenses": [{"name": "other"}],
    }
    (ASSETS / "dataset-metadata.json").write_text(
        json.dumps(metadata, indent=2) + "\n",
        encoding="utf-8",
    )


def notebook(ten_percent_only: bool):
    protocol_arguments = (
        '    "--protocol", "ten_percent",\n'
        '    "--sampling-seed", "101",\n'
        if ten_percent_only
        else ""
    )
    marker = (
        "QDENN_TEN_PERCENT_FIXED_SAMPLING_101_COMPLETE"
        if ten_percent_only
        else "QDENN_REMAINING_NOTEBOOK_COMPLETE"
    )
    code = """from pathlib import Path
import glob
import subprocess
import sys

subprocess.run([sys.executable, "-m", "pip", "install", "-q", "pennylane"], check=True)
root = Path(glob.glob("/kaggle/input/**/run_remaining.py", recursive=True)[0]).parent
command = [
    sys.executable, str(root / "run_remaining.py"),
    "--repo-root", "/kaggle/working",
    "--cache", str(root / "cache"),
    "--in-domain-models", str(root / "in_domain_models"),
    "--output", "/kaggle/working/results",
    "--epochs", "10",
    "--batch-size", "32",
""" + protocol_arguments + """]
print("COMMAND", " ".join(command), flush=True)
subprocess.run(command, check=True)
print(""" + repr(marker) + """, flush=True)
"""
    return {
        "cells": [{
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": code.splitlines(keepends=True),
        }],
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "name": "python3"},
            "language_info": {"name": "python"},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }


def stage_kernel(ten_percent_only: bool):
    KERNEL.mkdir(parents=True, exist_ok=True)
    (KERNEL / "run.ipynb").write_text(
        json.dumps(notebook(ten_percent_only), indent=1) + "\n",
        encoding="utf-8",
    )
    reference = (
        TEN_PERCENT_KERNEL_REF
        if ten_percent_only
        else REMAINING_KERNEL_REF
    )
    asset_ref = (
        TEN_PERCENT_ASSET_REF
        if ten_percent_only
        else REMAINING_ASSET_REF
    )
    metadata = {
        "id": reference,
        "title": reference.partition("/")[2],
        "code_file": "run.ipynb",
        "language": "python",
        "kernel_type": "notebook",
        "is_private": True,
        "enable_gpu": False,
        "enable_internet": True,
        "dataset_sources": [asset_ref],
        "competition_sources": [],
        "kernel_sources": [],
        "model_sources": [],
    }
    (KERNEL / "kernel-metadata.json").write_text(
        json.dumps(metadata, indent=2) + "\n",
        encoding="utf-8",
    )


def upload_assets(asset_ref: str):
    probe = subprocess.run(
        [
            sys.executable,
            "-m",
            "kaggle",
            "datasets",
            "status",
            asset_ref,
            "--format",
            "json",
        ],
        text=True,
        capture_output=True,
        env=command_env(),
    )
    action = "version" if probe.returncode == 0 else "create"
    arguments = ["datasets", action, "-p", str(ASSETS), "--dir-mode", "zip"]
    if action == "version":
        arguments += ["-m", "Update QDENN remaining protocol assets"]
    kaggle(*arguments)
    deadline = time.monotonic() + 900
    while time.monotonic() < deadline:
        status = json.loads(
            kaggle(
                "datasets",
                "status",
                asset_ref,
                "--format",
                "json",
                capture=True,
            ).stdout
        ).get("status")
        print(f"QDENN asset status={status}", flush=True)
        if status == "ready":
            return
        time.sleep(10)
    raise TimeoutError(f"{asset_ref} did not become ready")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--submit", action="store_true")
    parser.add_argument("--ten-percent-only", action="store_true")
    args = parser.parse_args()
    asset_ref = (
        TEN_PERCENT_ASSET_REF
        if args.ten_percent_only
        else REMAINING_ASSET_REF
    )
    stage_assets(asset_ref)
    stage_kernel(args.ten_percent_only)
    print(f"Staged QDENN remaining notebook under {STAGE}", flush=True)
    if not args.submit:
        return
    verify_account()
    upload_assets(asset_ref)
    kaggle("kernels", "push", "-p", str(KERNEL), "-t", "43200")
    reference = (
        TEN_PERCENT_KERNEL_REF
        if args.ten_percent_only
        else REMAINING_KERNEL_REF
    )
    print(f"Submitted {reference} CPU-only", flush=True)


if __name__ == "__main__":
    main()
