# Backend Architecture

**Status:** Draft baseline  
**Framework:** Python + FastAPI

## 1. Responsibilities

The backend is the authoritative application layer for authentication, persistence, simulation orchestration, content delivery, AI tools, analytics, and integration with future quantum providers.

## 2. Layering

```text
API / Routers
     ↓
Schemas / Validation
     ↓
Application Services
     ↓
Domain Services
     ↓
Repositories / External Providers
```

Routers should remain thin. Business logic belongs in service modules.

## 3. Service boundaries

### Quantum service

Responsible for:

- circuit validation;
- conversion to/from Quantum IR;
- Qiskit/Aer execution;
- result normalization;
- noise configuration;
- transpilation metadata;
- circuit hashing.

### Content service

Responsible for lesson lookup, curriculum hierarchy, prerequisites, experiments, media references, and content versioning.

### AI service

Responsible for agent orchestration, retrieval, context assembly, tool execution, safety/guardrail policy, streaming responses, and conversation persistence.

### Voice service

Responsible for speech-to-text and text-to-speech provider abstraction. Voice services should be asynchronous where generation time is non-trivial.

### Assessment service

Responsible for question delivery, answer validation, attempts, hints, grading, and progress updates.

## 4. API versioning

External API routes should be namespaced, for example `/api/v1/...`. Breaking changes require a new version or a migration strategy.

## 5. Error model

Use consistent machine-readable errors:

```json
{
  "error": {
    "code": "CIRCUIT_VALIDATION_ERROR",
    "message": "Controlled gate has an invalid target.",
    "requestId": "...",
    "details": {}
  }
}
```

Do not expose provider secrets, internal stack traces, or sandbox details to users.

## 6. Asynchronous work

Use a worker for:

- large simulations;
- embeddings;
- knowledge-base ingestion;
- voice generation;
- video preprocessing;
- expensive analytics.

A request should return a job identifier when the operation is asynchronous.

## 7. Authentication

Authentication should be provider-agnostic at the service boundary. Session or token validation occurs before resource-level authorization.

## 8. Authorization

Resources must be checked against ownership or role, not simply authentication status. A user may read public lessons but should only mutate circuits, conversations, and progress records they own or have explicit access to.

## 9. Configuration

Application configuration belongs in environment variables or a server-side secret manager. `.env.example` documents names and non-secret defaults; real credentials never belong in Git.

## 10. Testing

The backend test hierarchy should include:

- unit tests for domain services;
- API integration tests;
- deterministic quantum-reference tests;
- AI tool contract tests;
- database migration tests;
- end-to-end smoke tests.
