#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

cleanup() {
  kill "${API_PID:-}" "${WEB_PID:-}" 2>/dev/null || true
}
trap cleanup EXIT INT TERM

if command -v docker >/dev/null 2>&1; then
  docker compose up -d postgres redis
else
  echo "docker is not available; continuing with local services/default SQLite fallback."
fi

(
  cd apps/api
  PYTHON_BIN=".venv/bin/python"
  if [[ ! -x "$PYTHON_BIN" ]]; then
    echo "ERROR: apps/api/.venv is missing. Run ./scripts/setup.sh first." >&2
    exit 1
  fi
  exec "$PYTHON_BIN" -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
) &
API_PID=$!

(
  cd apps/web
  exec pnpm dev
) &
WEB_PID=$!

echo "Frontend: http://localhost:3000"
echo "Backend:  http://localhost:8000"
echo "Docs:     http://localhost:8000/docs"
echo "Press Ctrl+C to stop."

wait
