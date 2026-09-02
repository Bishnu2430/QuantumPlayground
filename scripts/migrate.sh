#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

if command -v docker >/dev/null 2>&1; then
  docker compose up -d postgres
  for _ in {1..30}; do
    if docker compose exec -T postgres pg_isready \
        -U "${POSTGRES_USER:-quantum}" \
        -d "${POSTGRES_DB:-quantum_lab}" >/dev/null 2>&1; then
      break
    fi
    sleep 2
  done
else
  echo "docker is not available; running migrations against configured DATABASE_URL/default SQLite."
fi

(
  cd apps/api
  PYTHON_BIN=".venv/bin/python"
  [[ -x "$PYTHON_BIN" ]] || { echo "ERROR: apps/api/.venv is missing. Run ./scripts/setup.sh first." >&2; exit 1; }
  "$PYTHON_BIN" -m alembic upgrade head
)

echo "Database migrations complete."
