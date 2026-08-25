# AI API

**Base path:** `/api/v1/ai`

## 1. Chat

### `POST /chat`

Accepts a user message plus optional context references:

```json
{
  "message": "Why does this Bell-state circuit only produce 00 and 11?",
  "lessonId": "lesson_bell",
  "circuitId": "c_123",
  "simulationId": "sim_456",
  "depth": "undergraduate"
}
```

The service may retrieve knowledge and call tools before returning an answer.

## 2. Streaming

### `POST /chat/stream`

Returns streamed tokens/events suitable for an interactive copilot.

Suggested event types:

```text
message_delta
source
thinking_state
tool_start
tool_result
circuit_patch
simulation_result
complete
error
```

Internal reasoning should never be exposed as chain-of-thought. `thinking_state` is a UI status such as `Searching sources…` or `Running simulation…`.

## 3. Explain selected content

### `POST /explain`

Accept selected text, equation, gate, circuit operation, or simulation output and return a context-aware explanation.

## 4. Circuit assistance

### `POST /circuit/suggest`

Proposes a circuit operation or algorithm construction plan.

### `POST /circuit/debug`

Analyzes a circuit together with its actual simulation output.

## 5. Code assistance

### `POST /code/explain`

Explains user code.

### `POST /code/generate`

Generates Qiskit code from a structured request.

### `POST /code/debug`

Analyzes syntax, API usage, and quantum-logic errors.

## 6. Sources

Every grounded response should be able to return source references used during retrieval. The frontend can display them inline or in a source drawer.
