# ADR 002: Start with Qiskit + Aer

**Status:** Accepted  
**Date:** 2026-08-25

## Context

The platform should eventually support multiple quantum software frameworks and execution providers. Supporting all of them during the hackathon would increase complexity in circuit conversion, testing, deployment, and content authoring.

## Decision

Use Qiskit as the first quantum programming backend and Qiskit Aer as the first local simulator. Hide it behind a backend adapter and expose only the platform Quantum IR to the rest of the application.

## Rationale

- Strong fit for Python-based educational execution.
- Local simulation avoids hardware dependency for the core demo.
- Mature circuit and transpilation concepts support future lessons.
- A stable adapter boundary makes future PennyLane/Cirq/OpenQASM support incremental rather than invasive.

## Consequences

### Positive

- Faster MVP delivery.
- One well-tested execution path.
- Clear separation between the educational product and framework-specific details.

### Negative

- Some framework-specific behavior will not be representable in the initial IR.
- Later multi-framework support may require IR extensions.

## Future adapters

Potential future adapters include PennyLane, Cirq, OpenQASM-based workflows, and cloud/QPU providers. Each must implement the same validation/compile/run/normalize contract.
