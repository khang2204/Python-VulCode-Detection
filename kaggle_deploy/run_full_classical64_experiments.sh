#!/usr/bin/env bash
# Run a fresh three-seed Classical-vs-Quantum experiment suite on Kaggle.
# Results are isolated under experiments/full_experiment_*; existing reported
# experiments and their logs are never overwritten.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PY="$ROOT/.venv/bin/python"
KAGGLE="$ROOT/.venv/bin/kaggle"
SEEDS=(101 202 303)
SPLIT_SEED=101
DATASETS=(benchmarkpython vudenc realvuln_human)
STAMP="$(date +%Y%m%d-%H%M%S)"
OUT="${OUT_DIR:-$ROOT/experiments/full_experiment_fixedsplit101_q10d5_lr002_$STAMP}"
POLL_SECONDS="${POLL_SECONDS:-60}"
mkdir -p "$OUT" "$OUT/in_domain/runs" "$OUT/logs"

[[ -x "$PY" && -x "$KAGGLE" ]] || { echo 'Missing .venv Python or Kaggle CLI.' >&2; exit 1; }
command -v jq >/dev/null || { echo 'jq is required.' >&2; exit 1; }

declare -A KERNEL=(
  [benchmarkpython]='khangtrn2/benchmarkpython-pag-vul-binary-training'
  [vudenc]='khangtrn2/vudenc-pag-vul-binary-training'
  [realvuln_human]='khangtrn2/realvuln-human-pag-vul-binary-training'
)

wait_for_run() {
  local kernel="$1" log="$2" started=0 status
  while :; do
    status="$($KAGGLE kernels status "$kernel" 2>&1)"
    printf '%s\n' "$status" | tee -a "$log"
    if [[ "$status" == *'RUNNING'* || "$status" == *'QUEUED'* ]]; then started=1; fi
    if [[ "$status" == *'ERROR'* || "$status" == *'CANCELLED'* ]]; then
      $KAGGLE kernels logs "$kernel" 2>&1 | tee -a "$log" || true
      return 1
    fi
    if (( started )) && [[ "$status" == *'COMPLETE'* ]]; then return 0; fi
    sleep "$POLL_SECONDS"
  done
}

download_output() {
  local kernel="$1" destination="$2"
  mkdir -p "$destination"
  "$KAGGLE" kernels output "$kernel" -p "$destination" --force
}

run_in_domain() {
  local dataset attention seed kernel work payload dest
  for dataset in "${DATASETS[@]}"; do
    kernel="${KERNEL[$dataset]}"
    for attention in classical quantum; do
      for seed in "${SEEDS[@]}"; do
        dest="$OUT/in_domain/runs/$dataset/$attention/seed_$seed"
        if [[ -f "$dest/gat_warmup_best.pt" && -f "$dest/pagvul_binary_best.pt" && -f "$dest/report.json" ]]; then
          echo "Skipping completed $dataset/$attention seed $seed"
          continue
        fi
        work="$OUT/in_domain/downloads/$dataset/$attention/seed_$seed"
        mkdir -p "$work"
        "$PY" "$ROOT/kaggle_deploy/in_domain/$dataset/deploy.py" --submit \
          --attention "$attention" --seed "$seed" --split-seed "$SPLIT_SEED" \
          2>&1 | tee "$OUT/logs/in_domain_${dataset}_${attention}_${seed}_submit.log"
        wait_for_run "$kernel" "$OUT/logs/in_domain_${dataset}_${attention}_${seed}_status.log"
        download_output "$kernel" "$work/output"
        payload="$(find "$work/output" -type f -name report.json -path "*${attention}*" -print -quit)"
        [[ -n "$payload" ]] || { echo "Missing $dataset/$attention/$seed report" >&2; exit 1; }
        payload="$(dirname "$payload")"
        mkdir -p "$dest"
        cp -a "$payload"/. "$dest"/
        [[ -f "$dest/gat_warmup_best.pt" && -f "$dest/pagvul_binary_best.pt" && -f "$dest/report.json" ]] || exit 1
      done
    done
  done
}

retain_benchmarkpython_quantum_audit() {
  local predictions="$OUT/in_domain/runs/benchmarkpython/quantum/seed_101/test_predictions.json"
  [[ -f "$predictions" ]] || { echo 'Missing BenchmarkPython Quantum seed_101 predictions for audit.' >&2; return 1; }
  "$PY" "$ROOT/kaggle_deploy/export_benchmarkpython_quantum_audit.py" \
    --predictions "$predictions" \
    --out-dir "$OUT/in_domain/audit/benchmarkpython_quantum_seed_101" \
    --count 2
}

refresh_sample_efficiency_assets() {
  local temp="$OUT/work/sample_efficiency_assets"
  mkdir -p "$temp"
  for dataset in "${DATASETS[@]}"; do
    cp "$OUT/in_domain/runs/$dataset/quantum/seed_$SPLIT_SEED/split_manifest.json" \
       "$temp/${dataset}_seed_${SPLIT_SEED}_split_manifest.json"
  done
  cp "$ROOT/kaggle_deploy/in_domain_ten_percent/run_sample_efficiency.py" \
     "$temp/run_sample_efficiency_q10.py"
  if [[ "$(<"$OUT/work/sample_efficiency_assets.ready" 2>/dev/null || true)" == 'Q10D5-LR002-HEAD50' ]] &&
     jq -e '.n_qubits == 10 and .quantum_depth == 5 and .learning_rate == 0.002 and .head_learning_rate == 0.002 and .head_epochs == 50' \
       "$temp/benchmarkpython_config.json" >/dev/null; then
    echo 'Sample-efficiency assets already match the current Q10D5 LR002 configuration; resuming.'
    return
  fi
  echo 'Refreshing stale sample-efficiency assets for the current Q10D5 LR002 configuration.'
  "$KAGGLE" datasets download -d khangtrn2/pagvul-sample-efficiency-assets -p "$temp" --unzip
  cp "$ROOT/train_pagvul_binary.py" "$ROOT/train_pagvul_classical.py" "$ROOT/train_pagvul_quantum.py" "$temp"/
  for dataset in "${DATASETS[@]}"; do
    cp "$OUT/in_domain/runs/$dataset/quantum/seed_$SPLIT_SEED/split_manifest.json" \
       "$temp/${dataset}_seed_${SPLIT_SEED}_split_manifest.json"
  done
  cp "$ROOT/kaggle_deploy/in_domain_ten_percent/run_sample_efficiency.py" \
     "$temp/run_sample_efficiency_q10.py"
  "$PY" - "$OUT/in_domain/runs" "$temp" <<'PY'
import json, sys
from pathlib import Path

runs, assets = map(Path, sys.argv[1:])
for dataset in ("benchmarkpython", "vudenc", "realvuln_human"):
    report = runs / dataset / "quantum" / "seed_101" / "report.json"
    config = json.loads(report.read_text(encoding="utf-8"))["config"]
    expected = {"n_qubits": 10, "quantum_depth": 5, "learning_rate": 0.002,
                "head_learning_rate": 0.002, "head_epochs": 50}
    if any(config[key] != value for key, value in expected.items()):
        raise RuntimeError(f"{report} does not contain the expected Q10D5 LR002 configuration")
    (assets / f"{dataset}_config.json").write_text(json.dumps(config, indent=2) + "\n", encoding="utf-8")
PY
  cat > "$temp/dataset-metadata.json" <<EOF
{"title":"PAG-Vul Sample-Efficiency Assets FixedSplit101 Q10D5 LR002","id":"khangtrn2/pagvul-sample-efficiency-assets","licenses":[{"name":"other"}]}
EOF
  printf 'uploading\n' > "$OUT/work/sample_efficiency_assets.ready"
  "$KAGGLE" datasets version -p "$temp" -m 'Q10 depth5 LR002 sample-efficiency assets' --dir-mode zip \
    2>&1 | tee "$OUT/logs/sample_efficiency_assets_upload.log"
  printf 'Q10D5-LR002-HEAD50\n' > "$OUT/work/sample_efficiency_assets.ready"
}

run_generalization() {
  local kernel='khangtrn2/pag-vul-cross-benchmark-generalization' work="$OUT/generalization"
  if [[ -f "$work/output/generalization_results/summary.md" ]]; then
    echo 'Skipping completed generalization.'
    return
  fi
  "$PY" "$ROOT/kaggle_deploy/generalization/deploy.py" --submit --runs-root "$OUT/in_domain/runs" \
    2>&1 | tee "$OUT/logs/generalization_submit.log"
  wait_for_run "$kernel" "$OUT/logs/generalization_status.log"
  download_output "$kernel" "$work/output"
}

run_ten_percent() {
  local kernel seed work report
  for seed in "${SEEDS[@]}"; do
    kernel="khangtrn2/pag-vul-ten-percent-seed-$seed"
    work="$OUT/in_domain_ten_percent/seed_$seed"
    if [[ -f "$work/output/ten_percent_results/report.json" ]]; then
      echo "Skipping completed Ten-percent seed $seed"
      continue
    fi
    PAGVUL_RUNS_ROOT="$OUT/in_domain/runs" "$PY" "$ROOT/kaggle_deploy/in_domain_ten_percent/submit.py" --submit --seed "$seed" --split-seed "$SPLIT_SEED" \
    --datasets "${DATASETS[@]}" --quantum-head-learning-rate 0.002 \
      2>&1 | tee "$OUT/logs/ten_percent_${seed}_submit.log"
    wait_for_run "$kernel" "$OUT/logs/ten_percent_${seed}_status.log"
    download_output "$kernel" "$work/output"
    report="$(find "$work/output" -name report.json -print -quit)"
    [[ -n "$report" ]] || exit 1
    "$PY" - "$report" "$seed" "$SPLIT_SEED" \
      "$ROOT/kaggle_deploy/in_domain_ten_percent/expected_subset_sha256.json" <<'PY'
import json, sys
from pathlib import Path

report = Path(sys.argv[1])
training_seed, split_seed = int(sys.argv[2]), int(sys.argv[3])
expected_subsets = json.loads(Path(sys.argv[4]).read_text(encoding="utf-8"))
payload = json.loads(report.read_text(encoding="utf-8"))
protocol = payload["protocol"]
expected = {
    "training_seed": training_seed,
    "fixed_split_seed": split_seed,
    "sampling_seed": 101,
}
actual = {key: protocol[key] for key in expected}
if actual != expected:
    raise RuntimeError(f"Ten-percent protocol mismatch: {actual} != {expected}")
for run in payload["runs"]:
    if run["training_seed"] != training_seed:
        raise RuntimeError(
            f'Ten-percent training seed mismatch for {run["dataset"]}: '
            f'{run["training_seed"]} != {training_seed}'
        )
    if not run.get("sampled_train_files") or not run.get("sampled_train_sha256"):
        raise RuntimeError(f'Ten-percent sample identity missing for {run["dataset"]}')
    expected_subset = expected_subsets["datasets"][run["dataset"]]
    actual_subset = {
        "samples": len(run["sampled_train_files"]),
        "sha256": run["sampled_train_sha256"],
    }
    if actual_subset != expected_subset:
        raise RuntimeError(
            f'Ten-percent subset mismatch for {run["dataset"]}: '
            f'{actual_subset} != {expected_subset}'
        )
PY
  done
}

run_long_tail() {
  local output="$OUT/long_tail_cwe_recall/long_tail_results.json"
  "$PY" "$ROOT/kaggle_deploy/long_tail_cwe_recall/evaluate_from_in_domain.py" \
    --runs-root "$OUT/in_domain/runs" \
    --metadata-root "$ROOT/CPG" \
    --output "$output"
  jq -e '.protocol.retraining == false and (.runs | length) == 18' \
    "$output" >/dev/null
}

printf 'Output root: %s\n' "$OUT" | tee "$OUT/README.txt"
if [[ "${ONLY_LONG_TAIL:-0}" == '1' ]]; then
  echo 'Running Long-tail only.'
  run_long_tail
else
  run_in_domain
  retain_benchmarkpython_quantum_audit
  refresh_sample_efficiency_assets
  run_generalization
  run_ten_percent
  run_long_tail
fi
printf 'Completed. All fresh reports: %s\n' "$OUT" | tee -a "$OUT/README.txt"
