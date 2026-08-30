#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

docker compose up -d postgres

for _ in {1..30}; do
  if docker compose exec -T postgres pg_isready \
      -U "${POSTGRES_USER:-quantum}" \
      -d "${POSTGRES_DB:-quantum_lab}" >/dev/null 2>&1; then
    break
  fi
  sleep 2
done

(
  cd apps/api
  uv run alembic upgrade head
)

echo "Database migrations complete."
