#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
KAGGLE="$ROOT/.venv/bin/kaggle"
KERNEL='khangtrn2/realvuln-human-pag-vul-binary-training'
STAMP="$(date +%Y%m%d-%H%M%S)"
RUN_DIR="$ROOT/kaggle_deploy/in_domain/realvuln_human/runs/$STAMP"
mkdir -p "$RUN_DIR/output"

"$KAGGLE" kernels status "$KERNEL" 2>&1 | tee "$RUN_DIR/status.txt" || true
"$KAGGLE" kernels logs "$KERNEL" 2>&1 | tee "$RUN_DIR/execution.log" || true
"$KAGGLE" kernels output "$KERNEL" -p "$RUN_DIR/output" --force 2>&1 | tee "$RUN_DIR/output_download.log" || true
printf 'Saved RealVuln Human diagnostics: %s\n' "$RUN_DIR"
