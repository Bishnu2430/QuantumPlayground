#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

cleanup() {
  kill "${API_PID:-}" "${WEB_PID:-}" 2>/dev/null || true
}
trap cleanup EXIT INT TERM

docker compose up -d postgres redis

(
  cd apps/api
  exec uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
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
