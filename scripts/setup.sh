#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

need() {
  command -v "$1" >/dev/null 2>&1 || {
    echo "ERROR: '$1' is required." >&2
    exit 1
  }
}

echo "== Quantum Lab setup =="

need git
need docker
need uv
need node
need pnpm

docker compose version >/dev/null

uv python install 3.13
uv python pin 3.13

[[ -f apps/api/pyproject.toml ]] || {
  echo "ERROR: apps/api/pyproject.toml not found." >&2
  exit 1
}
[[ -f apps/api/uv.lock ]] || {
  echo "ERROR: apps/api/uv.lock not found." >&2
  exit 1
}
[[ -f apps/web/package.json ]] || {
  echo "ERROR: apps/web/package.json not found." >&2
  exit 1
}
[[ -f apps/web/pnpm-lock.yaml ]] || {
  echo "ERROR: apps/web/pnpm-lock.yaml not found." >&2
  exit 1
}

(
  cd apps/api
  uv sync --all-extras --dev
)

(
  cd apps/web
  pnpm install --frozen-lockfile
)

if [[ ! -f .env && -f .env.example ]]; then
  cp .env.example .env
  echo "Created .env from .env.example. Review secrets before use."
fi

docker compose up -d postgres redis

echo
echo "Setup complete."
echo "Next:"
echo "  ./scripts/migrate.sh"
echo "  ./scripts/dev.sh"
