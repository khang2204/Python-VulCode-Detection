#!/usr/bin/env bash
# Save the current Kaggle status, execution log and completed output files.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
KAGGLE="$ROOT/.venv/bin/kaggle"
KERNEL="khangtrn2/benchmarkpython-pag-vul-binary-training"
STAMP="$(date +%Y%m%d-%H%M%S)"
RUN_DIR="$ROOT/kaggle_deploy/in_domain/benchmarkpython/runs/$STAMP"
mkdir -p "$RUN_DIR/output"

if "$KAGGLE" kernels status "$KERNEL" 2>&1 | tee "$RUN_DIR/status.txt"; then
  :
else
  printf '%s\n' 'Could not retrieve the current status.' | tee -a "$RUN_DIR/status.txt"
fi

if "$KAGGLE" kernels logs "$KERNEL" 2>&1 | tee "$RUN_DIR/execution.log"; then
  :
else
  printf '%s\n' 'Could not retrieve execution logs yet.' | tee -a "$RUN_DIR/execution.log"
fi

if "$KAGGLE" kernels output "$KERNEL" -p "$RUN_DIR/output" --force 2>&1 | tee "$RUN_DIR/output_download.log"; then
  :
else
  printf '%s\n' 'Output is not available yet (this is expected while the run is active).' | tee -a "$RUN_DIR/output_download.log"
fi

printf 'Saved Kaggle diagnostics: %s\n' "$RUN_DIR"
