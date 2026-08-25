# System Overview

**Status:** Draft baseline  
**Audience:** Engineering, AI, quantum, frontend, content, and hackathon demo teams  
**Scope:** Complete platform architecture

## 1. Product intent

Quantum Lab is an AI-native interactive quantum computing learning environment. It connects five modes of learning in one workflow:

1. theoretical explanation;
2. mathematical derivation and scientific reasoning;
3. visual and 3D representation;
4. executable quantum code and simulation; and
5. collaborative AI assistance.

The core product loop is:

`Learn → Derive → Visualize → Build → Execute → Observe → Ask → Modify → Re-run`

The platform must keep these representations synchronized. A concept page, equation, circuit, code snippet, simulation result, and AI explanation should all refer to the same underlying quantum model whenever possible.

## 2. Architectural goals

### Primary goals

- Make abstract quantum concepts observable and experimentally manipulable.
- Provide a single source of truth for quantum circuits through a framework-neutral internal representation.
- Run verified simulations instead of asking an LLM to invent quantum results.
- Ground AI answers in curated scientific content and live computational context.
- Make content modular so new concepts, experiments, algorithms, and visualizations can be added without frontend rewrites.
- Support an MVP on one machine while preserving a path to cloud deployment and optional hardware execution.

### Non-goals for the initial release

- Building a quantum compiler from first principles.
- Running arbitrary untrusted Python inside the API process.
- Supporting every quantum SDK on day one.
- Providing a full institutional LMS.
- Training a foundation model from scratch.

## 3. High-level system

```text
                     ┌────────────────────────────┐
                     │        Next.js Web         │
                     │ Lessons / Lab / Copilot    │
                     └──────────────┬─────────────┘
                                    │ HTTPS
                                    ▼
                     ┌────────────────────────────┐
                     │        FastAPI API         │
                     └───────┬──────────┬─────────┘
                             │          │
                 ┌───────────┘          └──────────────┐
                 ▼                                     ▼
       ┌──────────────────┐                  ┌──────────────────┐
       │  Quantum Engine  │                  │    AI Engine     │
       │ IR / Qiskit/Aer  │                  │ Agent / RAG/Tools │
       └────────┬─────────┘                  └────────┬─────────┘
                │                                    │
                └──────────────┬─────────────────────┘
                               ▼
                    ┌──────────────────────┐
                    │ PostgreSQL + pgvector│
                    │ Redis                 │
                    └──────────────────────┘
                               │
                               ▼
                       Background Workers
```

## 4. Major subsystems

| Subsystem | Responsibility |
|---|---|
| Web | Learning UI, circuit workspace, code editor, 3D visuals, AI interaction |
| API | Authentication, business logic, content delivery, simulation orchestration |
| Quantum Engine | Circuit validation, IR conversion, simulation, result normalization |
| AI Engine | Retrieval, tool use, tutoring, generation, debugging, personalization |
| Content System | Lessons, equations, experiments, media, prerequisites, references |
| Database | Users, progress, circuits, results, conversations, content metadata |
| Worker | Long-running simulations, indexing, voice generation, media jobs |
| Redis | Queues, cache, rate limits, transient job state |

## 5. Core request flows

### Learning flow

```text
User opens lesson
  → API fetches lesson metadata/content
  → frontend renders explanation/equations/visuals
  → embedded experiment loads
  → learner edits circuit
  → simulation request
  → quantum engine executes
  → normalized result returned
  → visualizations update
```

### AI explanation flow

```text
User asks question
  → AI agent classifies intent
  → retrieve relevant scientific context
  → inspect current lesson/circuit/result if needed
  → execute quantum tools if computation is required
  → generate grounded answer
  → attach citations / source metadata
```

### AI circuit creation flow

```text
Natural-language request
  → AI parses intent
  → tool selects circuit operation(s)
  → internal Quantum IR updated
  → frontend renders circuit
  → user reviews
  → optional simulation
```

## 6. Source-of-truth rules

The platform uses these priorities:

1. **Quantum execution result** is authoritative for numerical simulation output.
2. **Quantum IR** is authoritative for the current visual circuit.
3. **Curated content** is authoritative for educational claims unless an explicit research workflow says otherwise.
4. **LLM output** is an interpretation layer, not a source of truth for measurements or mathematical computation.
5. User-visible AI claims should include source context when the answer depends on external literature.

## 7. Deployment model

The canonical local environment is Docker Compose with separate `web`, `api`, `worker`, `postgres`, and `redis` services. Production can begin as the same container set on a single VPS and later move to managed databases or a container platform without changing application boundaries.

## 8. Reliability and observability

Every simulation and AI tool call should receive a unique request/job identifier. Log:

- user or anonymous session identifier;
- endpoint/tool name;
- circuit hash/version;
- backend used;
- execution duration;
- result status;
- AI model request metadata where permitted;
- error category.

Metrics should include request latency, simulation latency, job failures, AI tool success rate, lesson completion, and content retrieval hit rate.

## 9. Security principles

- Never execute arbitrary user Python inside the FastAPI process.
- Isolate code execution in a restricted worker or sandbox.
- Validate circuit operations before simulation.
- Store provider credentials only in server-side secrets.
- Apply authentication and authorization to user-owned resources.
- Rate-limit AI and simulation endpoints.
- Treat uploaded content as untrusted input.

## 10. Extensibility

The architecture intentionally separates framework-specific adapters from the internal circuit model. The initial implementation may support Qiskit + Aer only, while later adapters can target PennyLane, Cirq, OpenQASM, or cloud/QPU providers.
