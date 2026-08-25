# ADR 001: Use a Monorepo

**Status:** Accepted  
**Date:** 2026-08-25

## Context

The project contains a Next.js frontend, Python API/worker services, shared Quantum IR/schema definitions, content, knowledge-base ingestion scripts, infrastructure configuration, and documentation. The components evolve together and will be built rapidly during a hackathon.

## Decision

Use a single Git monorepo with clear application and package boundaries.

```text
apps/web
apps/api
packages/*
content/*
knowledge-base/*
infra/*
docs/*
```

Use pnpm workspaces for the JavaScript/TypeScript side and `uv` + `pyproject.toml` for Python.

## Rationale

- Shared schema changes can be reviewed atomically.
- Frontend/backend contracts remain close to implementation.
- One CI pipeline can validate the entire system.
- Content and code version together.
- Easier hackathon collaboration and deployment.

## Consequences

### Positive

- Simpler project navigation.
- Easier end-to-end changes.
- Single release point.

### Negative

- Repository becomes large over time.
- Teams need conventions to avoid unrelated coupling.
- CI should eventually use path-based optimization.

## Revisit when

Split repositories only if independent teams, release schedules, or access-control requirements make the monorepo a material bottleneck.
