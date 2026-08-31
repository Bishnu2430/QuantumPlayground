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

COMPOSE_FILES=(-f docker-compose.yml)
if [[ -f docker-compose.prod.yml ]]; then
  COMPOSE_FILES+=(-f docker-compose.prod.yml)
else
  echo "docker-compose.prod.yml not found; deploying with docker-compose.yml only."
fi

echo "Deploying Quantum Lab: ${IMAGE_TAG}"

docker compose "${COMPOSE_FILES[@]}" pull || true
docker compose "${COMPOSE_FILES[@]}" build
docker compose "${COMPOSE_FILES[@]}" up -d

sleep 5
docker compose "${COMPOSE_FILES[@]}" ps

./scripts/migrate.sh

echo "Deployment completed."
