#!/usr/bin/env python3
"""Stage, upload, submit, monitor, and download faithful QDENN in-domain runs.

This deployment is intentionally account-locked to ``ryhvic``.  Authentication
must be supplied through KAGGLE_API_TOKEN; the global Kaggle configuration is
never read or modified by this script.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path


HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parents[2]
STAGE = HERE / "kaggle_stage"
ASSET_STAGE = STAGE / "assets"
KERNEL_STAGE = STAGE / "kernel"
ASSET_REF = "ryhvic/qdenn-faithful-fixedsplit101-assets"
KERNEL_REFS = {
    "benchmarkpython": "ryhvic/faithful-qdenn-in-domain-benchmarkpython",
    "vudenc": "ryhvic/faithful-qdenn-in-domain-vudenc",
    "realvuln_human": "ryhvic/faithful-qdenn-in-domain-realvuln",
}
DATASETS = tuple(KERNEL_REFS)
TERMINAL = {"COMPLETE", "ERROR", "CANCELLED"}


def env() -> dict[str, str]:
    if not os.environ.get("KAGGLE_API_TOKEN"):
        raise SystemExit("KAGGLE_API_TOKEN is required; refusing to use global Kaggle config")
    return {**os.environ, "KAGGLE_API_TOKEN": os.environ["KAGGLE_API_TOKEN"]}


def kaggle(*arguments: str, capture: bool = False) -> subprocess.CompletedProcess:
    command = [sys.executable, "-m", "kaggle", *arguments]
    return subprocess.run(
        command,
        check=True,
        text=True,
        capture_output=capture,
        env=env(),
    )


def verify_account() -> dict:
    payload = json.loads(kaggle("quota", "--format", "json", capture=True).stdout)
    gpu = next(item for item in payload if item["resource"] == "GPU")
    mine = json.loads(
        kaggle("kernels", "list", "-m", "--format", "json", capture=True).stdout
    )
    if mine and any(not str(item["ref"]).startswith("ryhvic/") for item in mine):
        raise RuntimeError("Token does not resolve exclusively to the rhyvic account")
    print(
        f"Authenticated rhyvic; GPU remaining={gpu['remaining']} "
        f"(CPU kernels requested, GPU quota will not be used)",
        flush=True,
    )
    return gpu


def stage_assets() -> None:
    cache = ASSET_STAGE / "cache"
    expected = [
        cache / f"{dataset}_tokens_v2.pt"
        for dataset in DATASETS
    ]
    expected += [
        cache / f"{dataset}_split_v2_101.json"
        for dataset in DATASETS
    ]
    expected += [
        cache / f"{dataset}_vocab_v2_split_101.json"
        for dataset in DATASETS
    ]
    missing = [path for path in expected if not path.is_file()]
    if missing:
        raise SystemExit(f"Missing generated token cache: {missing[0]}")
    for name in ("models.py", "data.py", "run_in_domain.py", "FIDELITY.md"):
        shutil.copy2(HERE / name, ASSET_STAGE / name)
    metadata = {
        "title": "Faithful QDENN Fixed-Split-101 Assets",
        "id": ASSET_REF,
        "licenses": [{"name": "other"}],
    }
    (ASSET_STAGE / "dataset-metadata.json").write_text(
        json.dumps(metadata, indent=2) + "\n", encoding="utf-8"
    )


def asset_status() -> tuple[str, int]:
    probe = subprocess.run(
        [
            sys.executable,
            "-m",
            "kaggle",
            "datasets",
            "status",
            ASSET_REF,
            "--format",
            "json",
        ],
        text=True,
        capture_output=True,
        env=env(),
    )
    try:
        payload = json.loads(probe.stdout)
        return str(payload.get("status", "unknown")), int(
            payload.get("current_version_number", 0)
        )
    except (json.JSONDecodeError, TypeError, ValueError):
        return "missing", 0


def upload_assets() -> None:
    stage_assets()
    status, previous = asset_status()
    if previous:
        kaggle(
            "datasets",
            "version",
            "-p",
            str(ASSET_STAGE),
            "-m",
            "Faithful QDENN fixed-split-101 source and token cache",
            "--dir-mode",
            "zip",
        )
    else:
        kaggle(
            "datasets",
            "create",
            "-p",
            str(ASSET_STAGE),
            "--dir-mode",
            "zip",
        )
    target = previous + 1
    deadline = time.monotonic() + 900
    while time.monotonic() < deadline:
        status, version = asset_status()
        print(f"Asset dataset v{version}: {status}", flush=True)
        if status == "ready" and version >= target:
            return
        time.sleep(10)
    raise TimeoutError(f"Asset dataset v{target} did not become ready")


def notebook(dataset: str) -> dict:
    code = f"""from pathlib import Path
import glob
import subprocess
import sys

subprocess.run([sys.executable, "-m", "pip", "install", "-q", "pennylane"], check=True)
asset_root = Path(glob.glob("/kaggle/input/**/run_in_domain.py", recursive=True)[0]).parent
command = [
    sys.executable,
    str(asset_root / "run_in_domain.py"),
    "--model", "qdenn",
    "--dataset", "{dataset}",
    "--epochs", "10",
    "--output", "/kaggle/working/results",
    "--cache", str(asset_root / "cache"),
]
print("COMMAND", " ".join(command), flush=True)
log_path = Path("/kaggle/working/qdenn_{dataset}.log")
with log_path.open("a", encoding="utf-8", buffering=1) as log:
    process = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1,
    )
    for line in process.stdout:
        print(line, end="", flush=True)
        log.write(line)
    return_code = process.wait()
if return_code:
    raise SystemExit(return_code)
print("QDENN_IN_DOMAIN_COMPLETE {dataset}", flush=True)
"""
    return {
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "# Faithful QDENN in-domain\n",
                    f"Dataset: `{dataset}`; split seed: 101; training seeds: 101, 202, 303.\n",
                ],
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": code.splitlines(keepends=True),
            },
        ],
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "name": "python3"},
            "language_info": {"name": "python"},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }


def stage_kernel(dataset: str) -> Path:
    directory = KERNEL_STAGE / dataset
    directory.mkdir(parents=True, exist_ok=True)
    path = directory / "run.ipynb"
    path.write_text(json.dumps(notebook(dataset), indent=1) + "\n", encoding="utf-8")
    reference = KERNEL_REFS[dataset]
    metadata = {
        "id": reference,
        "title": reference.partition("/")[2],
        "code_file": "run.ipynb",
        "language": "python",
        "kernel_type": "notebook",
        "is_private": True,
        "enable_gpu": False,
        "enable_internet": True,
        "dataset_sources": [ASSET_REF],
        "competition_sources": [],
        "kernel_sources": [],
        "model_sources": [],
    }
    (directory / "kernel-metadata.json").write_text(
        json.dumps(metadata, indent=2) + "\n", encoding="utf-8"
    )
    return directory


def kernel_status(reference: str) -> str:
    probe = subprocess.run(
        [sys.executable, "-m", "kaggle", "kernels", "status", reference],
        text=True,
        capture_output=True,
        env=env(),
    )
    if probe.returncode:
        return "MISSING"
    match = re.search(r"KernelWorkerStatus\.([A-Z_]+)", probe.stdout)
    return match.group(1) if match else "UNKNOWN"


def wait_and_download(dataset: str, output_root: Path, poll_seconds: int) -> None:
    reference = KERNEL_REFS[dataset]
    destination = output_root / dataset
    destination.mkdir(parents=True, exist_ok=True)
    status_log = destination / "status.log"
    last = None
    while True:
        status = kernel_status(reference)
        timestamp = datetime.now().astimezone().isoformat(timespec="seconds")
        row = f"{timestamp} {reference} {status}\n"
        with status_log.open("a", encoding="utf-8") as stream:
            stream.write(row)
        if status != last:
            print(row, end="", flush=True)
            last = status
        if status in TERMINAL:
            break
        time.sleep(poll_seconds)
    kaggle("kernels", "output", reference, "-p", str(destination), "-o")
    if status != "COMPLETE":
        raise RuntimeError(f"{reference} ended with {status}; sequence stopped")
    reports = sorted(destination.rglob("report.json"))
    if len(reports) != 3:
        raise RuntimeError(
            f"{reference} completed but downloaded {len(reports)} reports, expected 3"
        )
    print(f"Downloaded and verified {len(reports)} reports for {dataset}", flush=True)


def submit(dataset: str) -> None:
    directory = stage_kernel(dataset)
    print(
        f"Submitting {KERNEL_REFS[dataset]} with CPU accelerator (GPU disabled)",
        flush=True,
    )
    kaggle("kernels", "push", "-p", str(directory), "-t", "43200")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--datasets",
        nargs="+",
        choices=DATASETS,
        default=list(DATASETS),
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=(
            REPO_ROOT
            / "QDENN_SOTA"
            / "experiments"
            / "results"
            / "qdenn_faithful_indomain_fixedsplit101"
        ),
    )
    parser.add_argument("--poll-seconds", type=int, default=60)
    parser.add_argument("--skip-assets", action="store_true")
    parser.add_argument("--stage-only", action="store_true")
    args = parser.parse_args()

    verify_account()
    if not args.skip_assets:
        upload_assets()
    for dataset in args.datasets:
        stage_kernel(dataset)
    if args.stage_only:
        print("Staging complete; nothing submitted", flush=True)
        return 0
    for dataset in args.datasets:
        report_dir = args.output / dataset / "results" / "in_domain" / "qdenn"
        if len(list(report_dir.rglob("report.json"))) == 3:
            print(f"Skipping locally complete dataset {dataset}", flush=True)
            continue
        status = kernel_status(KERNEL_REFS[dataset])
        if status not in {"RUNNING", "QUEUED", "PENDING", "COMPLETE"}:
            submit(dataset)
        else:
            print(
                f"Resuming monitor for {KERNEL_REFS[dataset]} in state {status}",
                flush=True,
            )
        wait_and_download(dataset, args.output, args.poll_seconds)
    print("All requested faithful QDENN in-domain datasets are complete", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
