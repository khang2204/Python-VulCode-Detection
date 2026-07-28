#!/usr/bin/env bash
# Submit a Kaggle run and keep the CLI transcript locally. This exits as soon
# as Kaggle accepts the run; monitor execution in the Kaggle browser UI.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
STAMP="$(date +%Y%m%d-%H%M%S)"
RUN_DIR="$ROOT/kaggle_deploy/in_domain/benchmarkpython/runs/$STAMP"
mkdir -p "$RUN_DIR"

MODE=(--submit)
for arg in "$@"; do
  if [[ "$arg" == "--kernel-only" ]]; then
    MODE=()
    break
  fi
done

"$ROOT/.venv/bin/python" "$ROOT/kaggle_deploy/in_domain/benchmarkpython/deploy.py" "${MODE[@]}" "$@" 2>&1 | tee "$RUN_DIR/submit.log"
printf '%s\n' "https://www.kaggle.com/code/khangtrn2/benchmarkpython-pag-vul-binary-training" > "$RUN_DIR/notebook_url.txt"
printf 'Saved submit transcript: %s\n' "$RUN_DIR/submit.log"
