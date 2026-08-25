# ADR 003: Use PostgreSQL + pgvector for the Initial RAG System

**Status:** Accepted  
**Date:** 2026-08-25

## Context

The AI tutor requires retrieval over curated quantum-science content. The project also needs a relational database for users, lessons, circuits, simulations, conversations, and progress. Introducing a separate vector database during the hackathon would add operational overhead.

## Decision

Use PostgreSQL as the primary database and pgvector for embeddings and similarity search during the initial release.

## Architecture

```text
Source documents
      ↓
Ingestion / chunking
      ↓
Embeddings
      ↓
PostgreSQL
   ├── relational metadata
   └── vector embeddings
      ↓
Retriever
      ↓
AI context builder
      ↓
LLM
```

## Rationale

- One operational system for most application state.
- Metadata filtering and vector retrieval can coexist.
- Easier local Docker setup.
- Simpler backup and migration story.
- Good fit for a curated, moderate-sized knowledge base.

## Retrieval strategy

Start with hybrid retrieval:

1. metadata filters for topic/difficulty/source;
2. vector similarity;
3. optional keyword search;
4. optional reranking;
5. source-aware context assembly.

## Content licensing rule

The platform must only ingest and redistribute source material it has the right to use. Copyrighted books can inform the curriculum design without being copied wholesale into a public retrieval corpus unless licensing permits it.

## Consequences

### Positive

- Low operational complexity.
- Easy developer setup.
- Strong consistency between content metadata and embeddings.

### Negative

- Extremely large corpora may eventually benefit from specialized retrieval infrastructure.
- Search tuning still requires evaluation.

## Revisit when

Move to specialized or distributed retrieval infrastructure if corpus size, latency, multi-tenant isolation, or ranking quality creates a measurable need.
