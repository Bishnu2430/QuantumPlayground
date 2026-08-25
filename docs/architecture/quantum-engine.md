# Quantum Engine

**Status:** Draft baseline  
**Primary backend:** Qiskit + Qiskit Aer  
**Extension path:** PennyLane, Cirq, OpenQASM, cloud/QPU adapters

## 1. Purpose

The Quantum Engine translates a framework-neutral circuit representation into an executable backend, runs the circuit, and normalizes outputs for visualization and AI inspection.

## 2. Internal representation

The platform owns a minimal Quantum IR. Example:

```json
{
  "numQubits": 2,
  "numClbits": 2,
  "operations": [
    {"gate": "h", "targets": [0], "moment": 0},
    {"gate": "cx", "controls": [0], "targets": [1], "moment": 1},
    {"gate": "measure", "targets": [0], "clbits": [0], "moment": 2},
    {"gate": "measure", "targets": [1], "clbits": [1], "moment": 2}
  ]
}
```

The exact schema belongs in `packages/quantum-schema/` and must be versioned.

## 3. Execution pipeline

```text
Quantum IR
  ↓
Schema validation
  ↓
Backend adapter
  ↓
Backend circuit
  ↓
Simulation / execution
  ↓
Raw result
  ↓
Normalized result
  ↓
Visualization + persistence + AI context
```

## 4. Initial Qiskit adapter

The first adapter supports the common gates and measurement operations required by the introductory curriculum. It should expose a small stable interface:

```python
class QuantumBackend:
    def validate(self, circuit): ...
    def compile(self, circuit): ...
    def run(self, circuit, options): ...
    def normalize(self, raw_result): ...
```

## 5. Simulation modes

### Statevector mode

Best for concept visualization, gate-by-gate state inspection, and small circuits.

### Shot mode

Runs repeated measurements and returns counts/probabilities.

### Noise mode

Adds configurable error channels and device-like noise for educational demonstrations.

### Future hardware mode

Sends compatible circuits through provider adapters. Queueing, authentication, pricing, and hardware availability remain provider concerns.

## 6. Normalized result model

```json
{
  "backend": "qiskit-aer",
  "numQubits": 2,
  "shots": 1024,
  "counts": {"00": 508, "11": 516},
  "probabilities": {"00": 0.49609375, "11": 0.50390625},
  "statevector": null,
  "durationMs": 31,
  "metadata": {}
}
```

Avoid returning backend-specific objects to the frontend.

## 7. Validation rules

The engine validates:

- qubit indices;
- classical bit indices;
- gate arity;
- control/target collisions;
- parameter count and numeric range where applicable;
- measurement mapping;
- unsupported operations;
- circuit size limits.

## 8. Determinism

Educational tests should use fixed seeds where the backend supports them. Tests should compare mathematical expectations rather than individual random shot sequences when appropriate.

## 9. Resource limits

The backend must enforce limits such as:

- maximum qubits for synchronous jobs;
- maximum shots;
- maximum circuit depth;
- maximum execution time;
- maximum output payload.

These limits protect the service from accidental or malicious resource exhaustion.

## 10. Future adapters

Framework adapters must compile from the same IR and map back into the same normalized result model. This ensures that adding a framework does not require rewriting lessons or visualizations.
