# Database Architecture

**Status:** Draft baseline  
**Database:** PostgreSQL  
**Vector extension:** pgvector  
**Cache/queue:** Redis

## 1. Design goals

- relational integrity for user/content data;
- versioned circuits and experiments;
- queryable learner progress;
- vector search for scientific content;
- clear separation of transactional data and derived analytics;
- easy local development through Docker.

## 2. Core entities

```text
User
 ├── Profile
 ├── Progress
 ├── Attempts
 ├── Circuits
 │    └── CircuitVersions
 ├── SimulationRuns
 └── Conversations

Content
 ├── Topic
 ├── Concept
 ├── Lesson
 ├── Equation
 ├── Experiment
 └── Media

Knowledge
 ├── Document
 ├── Chunk
 └── Embedding
```

## 3. Key tables

### users

Authentication identity and account metadata.

### lessons

Structured lesson records with slug, title, difficulty, content reference, and publication state.

### concepts

Atomic concepts used for prerequisite graphs, AI retrieval, and skill tracking.

### circuits

Current named user circuit. Stores ownership, title, IR version, and metadata.

### circuit_versions

Immutable snapshots for undo/history, reproducibility, and auditability.

### simulation_runs

References a circuit version, backend, execution options, status, result reference, and timings.

### conversations / messages

AI interaction history, with optional links to lesson/circuit/simulation context.

### progress

Per-user concept/lesson mastery and completion state.

### knowledge_documents / knowledge_chunks

Source records and searchable chunks with citation metadata and embeddings.

## 4. Vector search model

A knowledge chunk should contain:

```text
id
source_document_id
text
heading
topic
concept_ids
difficulty
page_or_section
license_or_usage_note
embedding
```

Use metadata filters before or alongside vector similarity where possible.

## 5. Circuit persistence

Store the versioned Quantum IR as canonical structured JSON. Optionally store generated Qiskit/OpenQASM representations as derived artifacts.

Never treat generated code as the canonical circuit model.

## 6. Simulation result storage

Store summary results in PostgreSQL. Large artifacts such as full statevectors or rendered assets can be moved to object storage later. For the MVP, only persist outputs necessary for the user history and analytics.

## 7. Redis usage

Redis may hold:

- job queue state;
- short-lived cache entries;
- rate-limit counters;
- temporary AI session state.

Redis should not be the source of truth for permanent user data.

## 8. Migrations

Alembic manages schema migrations. Every migration must be reversible where practical and tested against a fresh database and an upgraded database.

## 9. Indexing

Likely indexes include:

- user ownership fields;
- lesson slug;
- circuit owner + updated timestamp;
- simulation status + created timestamp;
- concept prerequisite relations;
- vector indexes for knowledge embeddings.

## 10. Privacy

Conversation history and learner analytics can be sensitive. Retention policies, deletion flows, and access controls should be explicit before public deployment.
