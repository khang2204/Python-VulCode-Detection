#!/usr/bin/env bash
# Submit VUDENC and save only the immediate CLI transcript. Kaggle continues
# independently; follow the printed notebook URL in the browser.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
STAMP="$(date +%Y%m%d-%H%M%S)"
RUN_DIR="$ROOT/kaggle_deploy/in_domain/vudenc/runs/$STAMP"
mkdir -p "$RUN_DIR"

MODE=(--submit)
for arg in "$@"; do
  if [[ "$arg" == "--kernel-only" ]]; then MODE=(); break; fi
done

"$ROOT/.venv/bin/python" "$ROOT/kaggle_deploy/in_domain/vudenc/deploy.py" "${MODE[@]}" "$@" 2>&1 | tee "$RUN_DIR/submit.log"
printf '%s\n' 'https://www.kaggle.com/code/khangtrn2/vudenc-pag-vul-binary-training' > "$RUN_DIR/notebook_url.txt"
printf 'Saved submit transcript: %s\n' "$RUN_DIR/submit.log"
