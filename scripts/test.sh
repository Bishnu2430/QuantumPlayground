#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

(
  cd apps/api
  uv run pytest -q
)

(
  cd apps/web
  pnpm lint
  pnpm build
)

echo "All tests passed."
