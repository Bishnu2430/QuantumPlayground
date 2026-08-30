---
id: qubit-state
type: concept
domain: qubits
title: The Qubit
summary: "A normalized pure state in a two-dimensional complex Hilbert space."
level: foundational
prerequisites: [vectors, complex-numbers]
tags: [qubit, statevector, amplitude, phase]
equations: [qubit-state, normalization]
visualizations: [bloch-sphere-basic]
experiments: [first-superposition]
references: [nielsen-chuang, gentle-introduction]
---

# The Qubit

A pure single-qubit state is written

$$|\psi\rangle = \alpha|0\rangle + \beta|1\rangle,$$

with

$$|\alpha|^2 + |\beta|^2 = 1.$$

The complex numbers $\alpha$ and $\beta$ are **amplitudes**. A computational-basis measurement returns `0` with probability $|\alpha|^2$ and `1` with probability $|\beta|^2$.

## Intuition

Do not picture a qubit as literally being “0 and 1 at once.” The quantum state contains amplitudes and relative phase information that determine the statistics of different measurements.

## Geometry

Every pure single-qubit state can be represented on the Bloch sphere, up to a physically irrelevant global phase. The polar and azimuthal coordinates encode the state's relative amplitudes and phase.

## Experiment

1. Start in $|0\rangle$.
2. Apply $H$.
3. Inspect the statevector.
4. Run 1024 shots.
5. Apply $H$ again and run again.

The second Hadamard reverses the first in an ideal circuit because $H^2=I$.

## Questions

- Why do probabilities use squared magnitudes?
- What information is lost if you only record measurement counts?
- What changes when the relative phase changes?

## Qiskit

```python
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

qc = QuantumCircuit(1, 1)
qc.h(0)
qc.measure(0, 0)

result = AerSimulator().run(qc, shots=1024).result()
print(result.get_counts())
```
