#!/usr/bin/env python3
"""Submit one isolated fixed-subset 10%-train QProto replicate."""
from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import time
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
BASE_KERNEL = HERE / "kernel"
ACCOUNT = "khangtrn2"


def cli() -> str:
    return str(ROOT / ".venv/bin/kaggle")


def run(*arguments: str, capture: bool = False) -> subprocess.CompletedProcess:
    print("+", " ".join(arguments), flush=True)
    return subprocess.run(
        arguments,
        check=True,
        text=True,
        capture_output=capture,
    )


def dataset_state(dataset_ref: str) -> tuple[str, int]:
    probe = subprocess.run(
        [cli(), "datasets", "status", dataset_ref, "--format", "json"],
        text=True,
        capture_output=True,
    )
    if probe.returncode:
        return "missing", 0
    try:
        payload = json.loads(probe.stdout)
        return str(payload.get("status", "unknown")), int(
            payload.get("current_version_number", 0)
        )
    except (json.JSONDecodeError, TypeError, ValueError):
        return "unknown", 0


def wait_for_dataset(dataset_ref: str, expected_version: int) -> None:
    deadline = time.monotonic() + 900
    while time.monotonic() < deadline:
        status, version = dataset_state(dataset_ref)
        if status == "ready" and version >= expected_version:
            return
        print(
            f"Waiting for {dataset_ref} version {expected_version}: "
            f"status={status}, version={version}",
            flush=True,
        )
        time.sleep(10)
    raise TimeoutError(
        f"{dataset_ref} did not reach ready version {expected_version}"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--sampling-seed", type=int, default=101)
    parser.add_argument("--split-seed", type=int, default=101)
    parser.add_argument(
        "--datasets",
        nargs="+",
        choices=("benchmarkpython", "vudenc", "realvuln_human"),
        default=("benchmarkpython", "vudenc", "realvuln_human"),
    )
    parser.add_argument("--quantum-head-learning-rate", type=float, default=0.002)
    parser.add_argument("--submit", action="store_true")
    args = parser.parse_args()

    dataset_ref = f"{ACCOUNT}/pagvul-ten-percent-runtime-seed-{args.seed}"
    kernel_ref = f"{ACCOUNT}/pag-vul-ten-percent-seed-{args.seed}"
    runtime = HERE / f"runtime_seed_{args.seed}"
    kernel = HERE / f"kernel_seed_{args.seed}"
    if runtime.exists():
        shutil.rmtree(runtime)
    if kernel.exists():
        shutil.rmtree(kernel)
    runtime.mkdir(parents=True)
    shutil.copytree(BASE_KERNEL, kernel)

    source = HERE / "run_sample_efficiency.py"
    shutil.copy2(source, runtime / "run_sample_efficiency.py")
    runs_root = Path(
        os.environ.get(
            "PAGVUL_RUNS_ROOT",
            ROOT / "experiments/repeated_evaluation/runs",
        )
    )
    for dataset in args.datasets:
        shutil.copy2(
            runs_root
            / dataset
            / "quantum"
            / f"seed_{args.split_seed}"
            / "split_manifest.json",
            runtime / f"{dataset}_seed_{args.split_seed}_split_manifest.json",
        )
    (runtime / "sample_efficiency_runtime.json").write_text(
        json.dumps({"scenario": "ten_percent_in_domain"}) + "\n"
    )
    (runtime / "ten_percent_config.json").write_text(
        json.dumps(
            {
                "training_seed": args.seed,
                "sampling_seed": args.sampling_seed,
                "split_seed": args.split_seed,
                "datasets": list(args.datasets),
                "quantum_head_learning_rate": args.quantum_head_learning_rate,
            }
        )
        + "\n"
    )
    (runtime / "dataset-metadata.json").write_text(
        json.dumps(
            {
                "title": f"PAG Vul Ten Percent Runtime Seed {args.seed}",
                "id": dataset_ref,
                "licenses": [{"name": "other"}],
            },
            indent=2,
        )
        + "\n"
    )

    metadata_path = kernel / "kernel-metadata.json"
    metadata = json.loads(metadata_path.read_text())
    metadata.pop("id_no", None)
    metadata["id"] = kernel_ref
    metadata["title"] = f"PAG Vul Ten Percent Seed {args.seed}"
    metadata["dataset_sources"] = [
        "khangtrn2/pagvul-sample-efficiency-assets",
        dataset_ref,
    ]
    metadata_path.write_text(json.dumps(metadata, indent=2) + "\n")

    if not args.submit:
        print(f"Staged runtime={runtime} kernel={kernel}")
        return

    _, previous_version = dataset_state(dataset_ref)
    if previous_version:
        run(
            cli(),
            "datasets",
            "version",
            "-p",
            str(runtime),
            "-m",
            f"fixed subset training seed {args.seed}",
            "--dir-mode",
            "zip",
        )
        expected_version = previous_version + 1
    else:
        run(cli(), "datasets", "create", "-p", str(runtime), "--dir-mode", "zip")
        expected_version = 1
    wait_for_dataset(dataset_ref, expected_version)
    run(cli(), "kernels", "push", "-p", str(kernel), "--accelerator", "NvidiaTeslaT4")
    print(json.dumps({"dataset": dataset_ref, "kernel": kernel_ref}))


if __name__ == "__main__":
    main()
