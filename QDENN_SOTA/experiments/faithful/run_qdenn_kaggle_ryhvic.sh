#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
TOKEN_FILE="/home/khang/.kaggle-ryhvic/access_token"

if [[ ! -s "$TOKEN_FILE" ]]; then
  echo "Missing rhyvic token: $TOKEN_FILE" >&2
  exit 1
fi

export KAGGLE_API_TOKEN
KAGGLE_API_TOKEN="$(<"$TOKEN_FILE")"

exec "$ROOT/.venv/bin/python" \
  "$ROOT/QDENN_SOTA/experiments/faithful/kaggle_qdenn_in_domain.py" \
  "$@"
