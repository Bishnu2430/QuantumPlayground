# Frontend Architecture

**Status:** Draft baseline  
**Framework:** Next.js + React + TypeScript  
**Primary concern:** High-fidelity educational and quantum-interaction experience

## 1. Responsibilities

The frontend is responsible for presentation, interaction, local UI state, visualization, editing, and orchestration of user-initiated API calls. It must not become the quantum-computation source of truth.

## 2. Application areas

Recommended top-level routes:

- `/` — landing and product introduction
- `/learn` — curriculum browser
- `/learn/[topic]/[lesson]` — lesson experience
- `/laboratory` — integrated quantum workspace
- `/simulator` — standalone circuit simulator
- `/experiments/[slug]` — guided experiments
- `/algorithms/[slug]` — algorithm walkthroughs
- `/playground` — open-ended experimentation
- `/copilot` — AI-focused workspace
- `/dashboard` — progress and user activity
- `/settings` — profile and preferences

## 3. Component boundaries

### Quantum UI

`CircuitCanvas`, `GatePalette`, `QubitLine`, `CircuitControls`, `CircuitInspector`.

The UI manipulates a frontend representation compatible with the backend Quantum IR. Every edit should be serializable and versionable.

### Visualization UI

Three.js / React Three Fiber components are used for:

- Bloch spheres;
- state vectors;
- rotating phase demonstrations;
- multi-qubit state illustrations;
- quantum-network scenes;
- algorithm animations;
- hardware topology views.

Use animation as a teaching mechanism, not decorative motion.

### Code editor

Monaco Editor provides the Python/Qiskit editing experience. The editor should support syntax highlighting, run/stop controls, error panels, and optional AI-generated suggestions.

### AI UI

`CopilotPanel` should support:

- text chat;
- streaming responses;
- context chips such as current lesson/circuit/result;
- explain selected content;
- apply circuit suggestion;
- code patch preview;
- voice controls;
- conversation history.

## 4. State management

Use local component state for transient UI, a lightweight client store for cross-component quantum workspace state, and server state caching for API data.

Suggested conceptual stores:

```text
circuitStore
lessonStore
simulationStore
uiStore
```

The circuit store should expose an immutable edit model so changes can be compared, undone, serialized, and sent to the API.

## 5. Circuit/code synchronization

The preferred flow is:

```text
Visual edit → Quantum IR → Qiskit code generation

Qiskit code → validated parser/translator → Quantum IR
```

The frontend should display explicit synchronization state, for example `Saved`, `Unsaved`, `Generated`, or `External code differs`.

## 6. Visualization contract

Visual components consume normalized simulation data instead of framework-specific Qiskit objects.

Example:

```ts
interface SimulationResult {
  statevector?: ComplexAmplitude[];
  probabilities?: Record<string, number>;
  counts?: Record<string, number>;
  numQubits: number;
  shots?: number;
  backend: string;
  durationMs: number;
}
```

This makes the renderer independent of the simulator implementation.

## 7. Accessibility

- Keyboard navigation for circuit controls.
- Captions and transcripts for video/audio.
- Reduced-motion support.
- Color should not be the only indication of quantum states or errors.
- Equations should have accessible descriptions where practical.

## 8. Performance

- Lazy-load heavy Three.js scenes.
- Split lesson content and algorithm visualizations by route.
- Avoid recomputing 3D scenes when only text changes.
- Use Web Workers for purely client-side visualization calculations when useful.
- Never send very large statevectors to the browser unnecessarily.

## 9. Visual design principles

The visual identity should feel like a scientific instrument rather than a generic LMS. Use a dark, high-contrast workspace for experiments and more readable layouts for theoretical content. Motion should correspond to conceptual events such as gate application, state rotation, interference, measurement, and collapse.
