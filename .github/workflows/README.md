# GitHub Actions

- `ci.yml`: frontend lint/build and backend compile/test checks.
- `test.yml`: focused backend, quantum, and AI tests.
- `build.yml`: builds and pushes Docker images to GHCR.
- `deploy.yml`: SSH deployment to a Docker host.

Production deployment requires these GitHub secrets:

- `DEPLOY_HOST`
- `DEPLOY_USER`
- `DEPLOY_SSH_KEY`
- `DEPLOY_PATH`
- `DEPLOY_PORT` (optional)
