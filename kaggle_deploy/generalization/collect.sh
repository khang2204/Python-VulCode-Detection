#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
KAGGLE="$ROOT/.venv/bin/kaggle"
STAMP="$(date +%Y%m%d-%H%M%S)"
DEST="$ROOT/kaggle_deploy/generalization/runs/$STAMP"
mkdir -p "$DEST/output"

"$KAGGLE" kernels output khangtrn2/pag-vul-cross-benchmark-generalization -p "$DEST/output" | tee "$DEST/output_download.log"
"$KAGGLE" kernels status khangtrn2/pag-vul-cross-benchmark-generalization | tee "$DEST/status.txt"
find "$DEST/output" -type f -maxdepth 4 -print
echo "Saved generalization diagnostics: $DEST"
