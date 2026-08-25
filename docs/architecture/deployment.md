# Deployment Architecture

**Status:** Draft baseline  
**Primary local environment:** Docker Compose  
**Target:** Cloud deployment with reproducible containers

## 1. Local stack

```text
Docker Compose
├── web       : Next.js
├── api       : FastAPI
├── worker    : background jobs / quantum execution
├── postgres  : application database + pgvector
└── redis     : queue / cache
```

The local environment should be close to production so that Docker images are exercised continuously during development.

## 2. Production baseline

For the hackathon, a single Linux VPS is sufficient:

```text
Internet
   ↓
TLS reverse proxy
   ↓
web + api + worker containers
   ↓
managed or containerized PostgreSQL / Redis
```

A managed PostgreSQL instance is preferable once the project has real users or important data.

## 3. CI/CD

GitHub Actions should run on every pull request:

1. frontend lint/typecheck/test;
2. backend lint/typecheck/test;
3. quantum reference tests;
4. build Docker images;
5. optional end-to-end smoke test.

Deployment can run from a protected branch after successful CI.

## 4. Environment configuration

Required configuration categories:

```text
APP_ENV
DATABASE_URL
REDIS_URL
AUTH_SECRET
LLM_API_KEY
EMBEDDING_API_KEY
STT_PROVIDER_KEY
TTS_PROVIDER_KEY
STORAGE_BUCKET
```

Use placeholders in `.env.example`. Never commit credentials.

## 5. Reverse proxy

Use a TLS-capable reverse proxy in front of application containers. Routes should separate the public web application and API while keeping provider credentials server-side.

## 6. Observability

Collect:

- structured logs;
- HTTP latency;
- worker/job latency;
- simulation success rate;
- AI tool errors;
- container health;
- database health.

For a hackathon, a lightweight logging stack is sufficient. Full distributed tracing can be added later.

## 7. Backups

Back up PostgreSQL before any production migration. Object storage assets and uploaded content should also be included in backup strategy when they become user-owned or irreplaceable.

## 8. Security checklist

- HTTPS everywhere in production.
- Non-root application containers where practical.
- Secret injection through environment/secret manager.
- Strict CORS policy.
- Rate limiting.
- Database not publicly exposed.
- Sandbox code execution isolated from the main API.
- Pin Docker image versions in deployment manifests.
- Run dependency and image vulnerability scans.

## 9. Scaling path

### Stage 1

One VPS, Docker Compose.

### Stage 2

Managed PostgreSQL/Redis and separate worker host.

### Stage 3

Container orchestration, autoscaling workers, object storage/CDN, dedicated observability.

The application should not require a rewrite between these stages.
