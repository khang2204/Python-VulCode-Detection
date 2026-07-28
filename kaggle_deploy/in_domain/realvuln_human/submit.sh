#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
STAMP="$(date +%Y%m%d-%H%M%S)"
RUN_DIR="$ROOT/kaggle_deploy/in_domain/realvuln_human/runs/$STAMP"
mkdir -p "$RUN_DIR"

"$ROOT/.venv/bin/python" "$ROOT/kaggle_deploy/in_domain/realvuln_human/deploy.py" --submit "$@" 2>&1 | tee "$RUN_DIR/submit.log"
printf '%s\n' 'https://www.kaggle.com/code/khangtrn2/realvuln-human-pag-vul-binary-training' > "$RUN_DIR/notebook_url.txt"
printf 'Saved submit transcript: %s\n' "$RUN_DIR/submit.log"
