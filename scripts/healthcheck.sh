#!/usr/bin/env bash
set -euo pipefail

API_URL="${API_URL:-http://localhost:8000}"
WEB_URL="${WEB_URL:-http://localhost:3000}"

check() {
  local name="$1"
  local url="$2"

  if curl --fail --silent --show-error --max-time 10 "$url" >/dev/null; then
    echo "OK   $name -> $url"
  else
    echo "FAIL $name -> $url" >&2
    return 1
  fi
}

check "API" "${API_URL}/health"
check "WEB" "${WEB_URL}"
