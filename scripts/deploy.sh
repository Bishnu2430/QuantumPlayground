#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

IMAGE_TAG="${1:-latest}"
export IMAGE_TAG

[[ -f .env ]] || {
  echo "ERROR: .env is required on the deployment host." >&2
  exit 1
}

echo "Deploying Quantum Lab: ${IMAGE_TAG}"

docker compose -f docker-compose.yml -f docker-compose.prod.yml pull || true
docker compose -f docker-compose.yml -f docker-compose.prod.yml build
docker compose -f docker-compose.yml -f docker-compose.prod.yml up -d

sleep 5
docker compose -f docker-compose.yml -f docker-compose.prod.yml ps

./scripts/migrate.sh

echo "Deployment completed."
