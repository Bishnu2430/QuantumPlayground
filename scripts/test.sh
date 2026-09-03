#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

(
  cd apps/api

  PYTHON_BIN=".venv/bin/python"

  if [[ ! -x "$PYTHON_BIN" ]]; then
    PYTHON_BIN="$(command -v python3 || command -v python)"
  fi

  if "$PYTHON_BIN" -c 'import pytest' >/dev/null 2>&1; then
    set +e
    "$PYTHON_BIN" -m pytest -q
    PYTEST_EXIT=$?
    set -e

    if [[ "$PYTEST_EXIT" -eq 5 ]]; then
      echo "No pytest tests found; running backend smoke scenario instead."
      "$PYTHON_BIN" ../../scripts/smoke-backend.py
    elif [[ "$PYTEST_EXIT" -ne 0 ]]; then
      exit "$PYTEST_EXIT"
    fi
  else
    echo "pytest is not installed; running backend smoke scenario instead."
    "$PYTHON_BIN" ../../scripts/smoke-backend.py
  fi
)

(
  cd apps/web
  pnpm lint
  pnpm build
)

echo "All tests passed."
