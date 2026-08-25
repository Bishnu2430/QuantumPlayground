```
quantum-lab/
│
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── CHANGELOG.md
├── .gitignore
├── .dockerignore
├── .editorconfig
├── .env.example
├── docker-compose.yml
├── docker-compose.prod.yml
├── Makefile
├── justfile
│
├── docs/
│   ├── architecture/
│   │   ├── system-overview.md
│   │   ├── frontend-architecture.md
│   │   ├── backend-architecture.md
│   │   ├── ai-architecture.md
│   │   ├── quantum-engine.md
│   │   ├── database.md
│   │   └── deployment.md
│   │
│   ├── api/
│   │   ├── authentication.md
│   │   ├── lessons.md
│   │   ├── circuits.md
│   │   ├── simulations.md
│   │   ├── ai.md
│   │   └── users.md
│   │
│   ├── content/
│   │   ├── content-schema.md
│   │   ├── lesson-format.md
│   │   └── visualization-format.md
│   │
│   └── decisions/
│       ├── 001-monorepo.md
│       ├── 002-qiskit-backend.md
│       └── 003-rag-architecture.md
│
├── apps/
│   │
│   ├── web/
│   │   ├── package.json
│   │   ├── next.config.ts
│   │   ├── tsconfig.json
│   │   ├── eslint.config.mjs
│   │   ├── postcss.config.mjs
│   │   ├── components.json
│   │   │
│   │   ├── public/
│   │   │   ├── images/
│   │   │   ├── icons/
│   │   │   ├── logos/
│   │   │   ├── videos/
│   │   │   └── fonts/
│   │   │
│   │   └── src/
│   │       ├── app/
│   │       │   ├── layout.tsx
│   │       │   ├── page.tsx
│   │       │   │
│   │       │   ├── learn/
│   │       │   │   ├── page.tsx
│   │       │   │   ├── [topic]/
│   │       │   │   │   └── page.tsx
│   │       │   │   └── [topic]/[lesson]/
│   │       │   │       └── page.tsx
│   │       │   │
│   │       │   ├── laboratory/
│   │       │   │   └── page.tsx
│   │       │   │
│   │       │   ├── simulator/
│   │       │   │   └── page.tsx
│   │       │   │
│   │       │   ├── experiments/
│   │       │   │   ├── page.tsx
│   │       │   │   └── [slug]/
│   │       │   │       └── page.tsx
│   │       │   │
│   │       │   ├── algorithms/
│   │       │   │   ├── page.tsx
│   │       │   │   └── [slug]/
│   │       │   │       └── page.tsx
│   │       │   │
│   │       │   ├── playground/
│   │       │   │   └── page.tsx
│   │       │   │
│   │       │   ├── copilot/
│   │       │   │   └── page.tsx
│   │       │   │
│   │       │   ├── dashboard/
│   │       │   │   └── page.tsx
│   │       │   │
│   │       │   └── settings/
│   │       │       └── page.tsx
│   │       │
│   │       ├── components/
│   │       │   │
│   │       │   ├── ui/
│   │       │   ├── layout/
│   │       │   ├── navigation/
│   │       │   ├── cards/
│   │       │   ├── dialogs/
│   │       │   │
│   │       │   ├── quantum/
│   │       │   │   ├── CircuitCanvas.tsx
│   │       │   │   ├── CircuitToolbar.tsx
│   │       │   │   ├── GatePalette.tsx
│   │       │   │   ├── QubitLine.tsx
│   │       │   │   ├── MeasurementResults.tsx
│   │       │   │   └── CircuitControls.tsx
│   │       │   │
│   │       │   ├── visualization/
│   │       │   │   ├── BlochSphere.tsx
│   │       │   │   ├── StateVector.tsx
│   │       │   │   ├── ProbabilityChart.tsx
│   │       │   │   ├── DensityMatrix.tsx
│   │       │   │   ├── AmplitudeVisualizer.tsx
│   │       │   │   ├── QuantumTimeline.tsx
│   │       │   │   └── QuantumNetwork.tsx
│   │       │   │
│   │       │   ├── editor/
│   │       │   │   ├── CodeEditor.tsx
│   │       │   │   ├── CodeConsole.tsx
│   │       │   │   └── ExecutionPanel.tsx
│   │       │   │
│   │       │   ├── ai/
│   │       │   │   ├── CopilotPanel.tsx
│   │       │   │   ├── ChatMessage.tsx
│   │       │   │   ├── SuggestionCard.tsx
│   │       │   │   ├── ExplainButton.tsx
│   │       │   │   └── VoiceControls.tsx
│   │       │   │
│   │       │   ├── lessons/
│   │       │   ├── experiments/
│   │       │   └── animations/
│   │       │
│   │       ├── lib/
│   │       │   ├── api/
│   │       │   ├── quantum/
│   │       │   ├── ai/
│   │       │   ├── visualization/
│   │       │   ├── auth/
│   │       │   └── utils/
│   │       │
│   │       ├── hooks/
│   │       │   ├── useCircuit.ts
│   │       │   ├── useSimulation.ts
│   │       │   ├── useCopilot.ts
│   │       │   └── useVoice.ts
│   │       │
│   │       ├── stores/
│   │       │   ├── circuitStore.ts
│   │       │   ├── lessonStore.ts
│   │       │   ├── simulationStore.ts
│   │       │   └── uiStore.ts
│   │       │
│   │       ├── types/
│   │       │   ├── quantum.ts
│   │       │   ├── circuit.ts
│   │       │   ├── simulation.ts
│   │       │   ├── lessons.ts
│   │       │   └── ai.ts
│   │       │
│   │       └── styles/
│   │           └── globals.css
│   │
│   └── api/
│       ├── pyproject.toml
│       ├── uv.lock
│       ├── alembic.ini
│       ├── Dockerfile
│       │
│       ├── app/
│       │   ├── main.py
│       │   │
│       │   ├── api/
│       │   │   ├── router.py
│       │   │   └── v1/
│       │   │       ├── auth.py
│       │   │       ├── users.py
│       │   │       ├── lessons.py
│       │   │       ├── circuits.py
│       │   │       ├── simulation.py
│       │   │       ├── algorithms.py
│       │   │       ├── experiments.py
│       │   │       ├── copilot.py
│       │   │       ├── voice.py
│       │   │       └── progress.py
│       │   │
│       │   ├── core/
│       │   │   ├── config.py
│       │   │   ├── security.py
│       │   │   ├── logging.py
│       │   │   └── exceptions.py
│       │   │
│       │   ├── db/
│       │   │   ├── database.py
│       │   │   ├── session.py
│       │   │   └── models/
│       │   │       ├── user.py
│       │   │       ├── lesson.py
│       │   │       ├── circuit.py
│       │   │       ├── simulation.py
│       │   │       ├── progress.py
│       │   │       └── conversation.py
│       │   │
│       │   ├── schemas/
│       │   │   ├── auth.py
│       │   │   ├── users.py
│       │   │   ├── lessons.py
│       │   │   ├── circuits.py
│       │   │   ├── simulations.py
│       │   │   ├── ai.py
│       │   │   └── progress.py
│       │   │
│       │   ├── services/
│       │   │   ├── quantum/
│       │   │   │   ├── simulator.py
│       │   │   │   ├── circuit_parser.py
│       │   │   │   ├── circuit_validator.py
│       │   │   │   ├── statevector.py
│       │   │   │   ├── measurements.py
│       │   │   │   ├── noise.py
│       │   │   │   └── transpiler.py
│       │   │   │
│       │   │   ├── ai/
│       │   │   │   ├── agent.py
│       │   │   │   ├── prompts.py
│       │   │   │   ├── tools.py
│       │   │   │   ├── router.py
│       │   │   │   ├── guardrails.py
│       │   │   │   └── memory.py
│       │   │   │
│       │   │   ├── rag/
│       │   │   │   ├── ingestion.py
│       │   │   │   ├── chunker.py
│       │   │   │   ├── embeddings.py
│       │   │   │   ├── retriever.py
│       │   │   │   └── reranker.py
│       │   │   │
│       │   │   ├── voice/
│       │   │   │   ├── speech_to_text.py
│       │   │   │   ├── text_to_speech.py
│       │   │   │   └── narration.py
│       │   │   │
│       │   │   ├── content/
│       │   │   │   ├── lesson_service.py
│       │   │   ├── assessment/
│       │   │   └── analytics/
│       │   │
│       │   └── workers/
│       │       ├── embedding_worker.py
│       │       ├── voice_worker.py
│       │       └── simulation_worker.py
│       │
│       └── tests/
│           ├── unit/
│           ├── integration/
│           ├── quantum/
│           └── ai/
│
├── packages/
│   ├── quantum-schema/
│   │   ├── circuit.schema.json
│   │   └── README.md
│   │
│   ├── quantum-ir/
│   │   ├── README.md
│   │   └── specification.md
│   │
│   └── ui/
│       └── shared-components/
│
├── content/
│   │
│   ├── curriculum/
│   │   ├── 00-introduction/
│   │   ├── 01-quantum-physics/
│   │   ├── 02-mathematics/
│   │   ├── 03-qubits/
│   │   ├── 04-quantum-gates/
│   │   ├── 05-multi-qubit-systems/
│   │   ├── 06-entanglement/
│   │   ├── 07-measurement/
│   │   ├── 08-quantum-algorithms/
│   │   ├── 09-cryptography/
│   │   ├── 10-error-correction/
│   │   ├── 11-quantum-hardware/
│   │   ├── 12-noise/
│   │   ├── 13-vqe-qaoa/
│   │   ├── 14-qml/
│   │   ├── 15-quantum-information/
│   │   ├── 16-quantum-networks/
│   │   ├── 17-quantum-sensing/
│   │   ├── 18-quantum-foundations/
│   │   └── 19-advanced-topics/
│   │
│   ├── lessons/
│   │   ├── qubit.md
│   │   ├── superposition.md
│   │   ├── measurement.md
│   │   ├── bloch-sphere.md
│   │   ├── entanglement.md
│   │   ├── teleportation.md
│   │   ├── grover.md
│   │   └── ...
│   │
│   ├── equations/
│   │   ├── qubit.yaml
│   │   ├── gates.yaml
│   │   ├── entanglement.yaml
│   │   └── algorithms.yaml
│   │
│   ├── experiments/
│   │   ├── double-slit/
│   │   ├── bell-state/
│   │   ├── teleportation/
│   │   ├── grover/
│   │   ├── qaoa/
│   │   └── noise/
│   │
│   ├── visualizations/
│   │   ├── bloch-sphere/
│   │   ├── double-slit/
│   │   ├── teleportation/
│   │   └── algorithms/
│   │
│   ├── videos/
│   │   ├── fundamentals/
│   │   ├── algorithms/
│   │   └── experiments/
│   │
│   ├── images/
│   │   ├── diagrams/
│   │   ├── illustrations/
│   │   └── historical/
│   │
│   └── references/
│       ├── books/
│       ├── papers/
│       ├── documentation/
│       └── citations.yaml
│
├── knowledge-base/
│   ├── raw/
│   │   ├── books/
│   │   ├── papers/
│   │   ├── lecture-notes/
│   │   └── documentation/
│   │
│   ├── processed/
│   │   ├── chunks/
│   │   ├── metadata/
│   │   └── concepts/
│   │
│   ├── indexes/
│   │   └── README.md
│   │
│   └── ingestion/
│       ├── ingest.py
│       ├── clean.py
│       ├── chunk.py
│       └── index.py
│
├── simulation-assets/
│   ├── circuits/
│   ├── statevectors/
│   ├── animations/
│   └── datasets/
│
├── infra/
│   ├── docker/
│   │   ├── web.Dockerfile
│   │   ├── api.Dockerfile
│   │   └── worker.Dockerfile
│   │
│   ├── nginx/
│   │   └── nginx.conf
│   │
│   ├── postgres/
│   │   └── init.sql
│   │
│   ├── redis/
│   │   └── redis.conf
│   │
│   └── monitoring/
│       └── ...
│
├── scripts/
│   ├── dev.sh
│   ├── setup.sh
│   ├── seed-db.py
│   ├── ingest-knowledge.py
│   ├── generate-embeddings.py
│   └── validate-content.py
│
├── .github/
│   └── workflows/
│       ├── ci.yml
│       ├── test.yml
│       ├── build.yml
│       └── deploy.yml
│
└── notebooks/
    ├── quantum-experiments/
    ├── algorithm-research/
    └── ai-evaluation/
```
