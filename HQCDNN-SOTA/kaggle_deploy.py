#!/usr/bin/env python3
"""Stage or submit standalone HQCDNN CPU notebooks.

No Kaggle request is made unless ``--submit`` is supplied. Authentication is
read only from KAGGLE_API_TOKEN; global Kaggle configuration is never changed.
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path

from common import DATASETS, fixed_manifest, load_records

HERE = Path(__file__).resolve().parent
STAGE = HERE / "kaggle_stage"
ASSETS = STAGE / "assets"
KERNELS = STAGE / "kernels"
PROTOCOLS = ("in_domain", "generalization", "ten_percent", "long_tail")
REMAINING_PROTOCOLS = ("generalization", "ten_percent", "long_tail")


def command_env():
    token = os.environ.get("KAGGLE_API_TOKEN")
    if not token:
        raise SystemExit("KAGGLE_API_TOKEN is required with --submit")
    return {**os.environ, "KAGGLE_API_TOKEN": token}


def kaggle(*arguments, capture=False):
    return subprocess.run(
        [sys.executable, "-m", "kaggle", *arguments],
        check=True, text=True, capture_output=capture, env=command_env(),
    )


def verify_account(account):
    mine = json.loads(
        kaggle("kernels", "list", "-m", "--format", "json", capture=True).stdout
    )
    if mine and any(not str(item["ref"]).startswith(f"{account}/") for item in mine):
        raise RuntimeError(f"Token does not resolve exclusively to {account}")


def stage_assets(repo_root: Path, account: str, include_pretrained: bool = False):
    ASSETS.mkdir(parents=True, exist_ok=True)
    cache = ASSETS / "cache"
    for dataset in DATASETS:
        records = load_records(repo_root, dataset, cache)
        fixed_manifest(records, cache, dataset)
    for name in ("common.py", "model.py", "run_experiments.py", "README.md"):
        shutil.copy2(HERE / name, ASSETS / name)
    if include_pretrained:
        source_root = HERE / "experiments" / "results" / "in_domain" / "results"
        destination_root = ASSETS / "pretrained_in_domain"
        if destination_root.exists():
            shutil.rmtree(destination_root)
        for qubits in (2, 4):
            for dataset in DATASETS:
                for seed in (101, 202, 303):
                    source = (
                        source_root
                        / f"{qubits}q"
                        / "in_domain"
                        / dataset
                        / f"seed_{seed}"
                    )
                    for name in ("model.pt", "tfidf.pt"):
                        source_file = source / name
                        if not source_file.is_file():
                            raise FileNotFoundError(source_file)
                        target = (
                            destination_root
                            / f"{qubits}q"
                            / dataset
                            / f"seed_{seed}"
                            / name
                        )
                        target.parent.mkdir(parents=True, exist_ok=True)
                        shutil.copy2(source_file, target)
    metadata = {
        "title": "HQCDNN fixed-split-101 source and records",
        "id": f"{account}/hqcdnn-fixedsplit101-assets",
        "licenses": [{"name": "other"}],
    }
    (ASSETS / "dataset-metadata.json").write_text(
        json.dumps(metadata, indent=2) + "\n", encoding="utf-8"
    )


def notebook(protocol: str, qubits: list[int]):
    code = f"""from pathlib import Path
import glob
import subprocess
import sys

subprocess.run([sys.executable, "-m", "pip", "install", "-q", "pennylane"], check=True)
root = Path(glob.glob("/kaggle/input/**/run_experiments.py", recursive=True)[0]).parent
for qubits in {qubits!r}:
    command = [
        sys.executable, str(root / "run_experiments.py"),
        "--repo-root", "/kaggle/working",
        "--cache", str(root / "cache"),
        "--output", "/kaggle/working/results",
        "--protocol", "{protocol}",
        "--dataset", "all",
        "--qubits", str(qubits),
        "--sampling-seed", "101",
    ]
    print("COMMAND", " ".join(command), flush=True)
    subprocess.run(command, check=True)
print("HQCDNN_{protocol.upper()}_COMPLETE", flush=True)
"""
    return {
        "cells": [{
            "cell_type": "code", "execution_count": None, "metadata": {},
            "outputs": [], "source": code.splitlines(keepends=True),
        }],
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "name": "python3"},
            "language_info": {"name": "python"},
        },
        "nbformat": 4, "nbformat_minor": 5,
    }


def remaining_notebook(qubits: list[int]):
    code = f"""from pathlib import Path
import glob
import subprocess
import sys

subprocess.run([sys.executable, "-m", "pip", "install", "-q", "pennylane"], check=True)
root = Path(glob.glob("/kaggle/input/**/run_experiments.py", recursive=True)[0]).parent
for qubits in {qubits!r}:
    for protocol in {list(REMAINING_PROTOCOLS)!r}:
        command = [
            sys.executable, str(root / "run_experiments.py"),
            "--repo-root", "/kaggle/working",
            "--cache", str(root / "cache"),
            "--output", "/kaggle/working/results",
            "--protocol", protocol,
            "--dataset", "all",
            "--qubits", str(qubits),
            "--sampling-seed", "101",
            "--pretrained-in-domain", str(root / "pretrained_in_domain"),
        ]
        print("COMMAND", " ".join(command), flush=True)
        subprocess.run(command, check=True)
print("HQCDNN_REMAINING_COMPLETE", flush=True)
"""
    return {
        "cells": [{
            "cell_type": "code", "execution_count": None, "metadata": {},
            "outputs": [], "source": code.splitlines(keepends=True),
        }],
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "name": "python3"},
            "language_info": {"name": "python"},
        },
        "nbformat": 4, "nbformat_minor": 5,
    }


def stage_kernels(account: str, protocols: list[str], qubits: list[int]):
    for protocol in protocols:
        directory = KERNELS / protocol
        directory.mkdir(parents=True, exist_ok=True)
        (directory / "run.ipynb").write_text(
            json.dumps(notebook(protocol, qubits), indent=1) + "\n",
            encoding="utf-8",
        )
        reference = f"{account}/hqcdnn-{protocol.replace('_', '-')}"
        metadata = {
            "id": reference,
            "title": reference.partition("/")[2],
            "code_file": "run.ipynb",
            "language": "python",
            "kernel_type": "notebook",
            "is_private": True,
            "enable_gpu": False,
            "enable_internet": True,
            "dataset_sources": [f"{account}/hqcdnn-fixedsplit101-assets"],
            "competition_sources": [], "kernel_sources": [], "model_sources": [],
        }
        (directory / "kernel-metadata.json").write_text(
            json.dumps(metadata, indent=2) + "\n", encoding="utf-8"
        )


def stage_remaining_kernel(account: str, qubits: list[int]):
    directory = KERNELS / "remaining"
    directory.mkdir(parents=True, exist_ok=True)
    (directory / "run.ipynb").write_text(
        json.dumps(remaining_notebook(qubits), indent=1) + "\n",
        encoding="utf-8",
    )
    reference = f"{account}/hqcdnn-remaining-fixed-split-101"
    metadata = {
        "id": reference,
        "title": "HQCDNN remaining fixed-split-101",
        "code_file": "run.ipynb",
        "language": "python",
        "kernel_type": "notebook",
        "is_private": True,
        "enable_gpu": False,
        "enable_internet": True,
        "dataset_sources": [f"{account}/hqcdnn-fixedsplit101-assets"],
        "competition_sources": [],
        "kernel_sources": [],
        "model_sources": [],
    }
    (directory / "kernel-metadata.json").write_text(
        json.dumps(metadata, indent=2) + "\n",
        encoding="utf-8",
    )


def upload_assets(account: str):
    probe = subprocess.run(
        [
            sys.executable, "-m", "kaggle", "datasets", "status",
            f"{account}/hqcdnn-fixedsplit101-assets", "--format", "json",
        ],
        text=True, capture_output=True, env=command_env(),
    )
    action = "version" if probe.returncode == 0 else "create"
    arguments = ["datasets", action, "-p", str(ASSETS), "--dir-mode", "zip"]
    if action == "version":
        arguments += ["-m", "Update fixed-split HQCDNN source and records"]
    kaggle(*arguments)
    reference = f"{account}/hqcdnn-fixedsplit101-assets"
    deadline = time.monotonic() + 900
    while time.monotonic() < deadline:
        status_probe = subprocess.run(
            [
                sys.executable, "-m", "kaggle", "datasets", "status",
                reference, "--format", "json",
            ],
            text=True, capture_output=True, env=command_env(),
        )
        try:
            status = json.loads(status_probe.stdout).get("status", "unknown")
        except (json.JSONDecodeError, AttributeError):
            status = "unknown"
        print(f"Asset dataset status: {status}", flush=True)
        if status == "ready":
            return
        time.sleep(10)
    raise TimeoutError(f"{reference} did not become ready within 15 minutes")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, required=True)
    parser.add_argument("--account", required=True)
    parser.add_argument(
        "--protocol", nargs="+", choices=PROTOCOLS, default=list(PROTOCOLS)
    )
    parser.add_argument("--qubits", type=int, nargs="+", choices=(2, 4), default=[2, 4])
    parser.add_argument(
        "--remaining-combined",
        action="store_true",
        help="Stage/submit one CPU notebook for generalization, ten-percent, and long-tail.",
    )
    parser.add_argument("--submit", action="store_true")
    args = parser.parse_args()
    stage_assets(
        args.repo_root,
        args.account,
        include_pretrained=args.remaining_combined,
    )
    if args.remaining_combined:
        stage_remaining_kernel(args.account, args.qubits)
    else:
        stage_kernels(args.account, args.protocol, args.qubits)
    print(f"Staged HQCDNN under {STAGE}", flush=True)
    if not args.submit:
        print("Stage-only mode: no Kaggle API request was made", flush=True)
        return
    verify_account(args.account)
    upload_assets(args.account)
    if args.remaining_combined:
        kaggle("kernels", "push", "-p", str(KERNELS / "remaining"), "-t", "43200")
    else:
        for protocol in args.protocol:
            kaggle("kernels", "push", "-p", str(KERNELS / protocol), "-t", "43200")
    print("Submitted requested HQCDNN CPU notebooks", flush=True)


if __name__ == "__main__":
    main()
