---
id: first-qiskit-circuit
type: lesson
domain: introduction
title: "Your First Qiskit Circuit"
summary: "Build a two-qubit Bell circuit, simulate it, and connect the diagram to its measured counts."
level: beginner
audience: [undergraduate, beginner, engineer]
tags: [introduction, qiskit, circuits, measurement]
equations: [bell-state, born-rule]
visualizations: [bell-state-correlations, probability-bars]
experiments: [bell-state]
references:
  [
    qiskit-hello-world-2026,
    qiskit-aer-simulation-2026,
    qiskit-visualization-2026,
  ]
---

# Your First Qiskit Circuit

## What this means

A Qiskit circuit is an ordered program for quantum and classical registers. The circuit below prepares two qubits, creates correlation with a Hadamard gate followed by a controlled-X, and samples the result by measuring both qubits.

## Build the intuition

Both qubits begin in $|00\rangle$. The Hadamard gate puts qubit 0 into an equal superposition. The controlled-X flips qubit 1 only on the branch where qubit 0 is $|1\rangle$. The two branches become $|00\rangle$ and $|11\rangle$, so measurements agree even though each individual result is unpredictable.

## Formal statement

The circuit prepares the Bell state

$$|\Phi^+\rangle = \frac{|00\rangle + |11\rangle}{\sqrt{2}}.$$

The state is normalized because

$$\left|\frac{1}{\sqrt{2}}\right|^2 + \left|\frac{1}{\sqrt{2}}\right|^2 = \frac12 + \frac12 = 1.$$

## Mathematical lens

Starting with $|00\rangle$:

$$H\otimes I|00\rangle = \frac{|00\rangle + |10\rangle}{\sqrt{2}}.$$

The controlled-X maps $|10\rangle$ to $|11\rangle$ and leaves $|00\rangle$ unchanged:

$$CX\frac{|00\rangle + |10\rangle}{\sqrt{2}} = \frac{|00\rangle + |11\rangle}{\sqrt{2}}.$$

By the Born rule, each measured string has probability $|1/\sqrt{2}|^2=1/2$. Finite shots fluctuate around that value.

## Visual lens

Use the circuit view to follow time from left to right. Use the probability bars to compare the ideal prediction, $P(00)=P(11)=0.5$, with the sampled counts. Qiskit displays classical bit strings using its documented bit-ordering convention; check the register labels before interpreting a multi-qubit result.

## Experiment

Before running, predict which strings can appear and whether `01` or `10` should occur. Run 1024 shots, compare the counts, then change `cx(0, 1)` to `x(1)` and explain why the correlation disappears.

## Code example

```python
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)
qc.measure([0, 1], [0, 1])

result = AerSimulator(seed_simulator=42).run(qc, shots=1024).result()
print(result.get_counts())
```

## Common misconceptions

- A measurement result is sampled; it is not a hidden fixed pair of classical bits.
- The Bell state is not the same thing as a 50/50 classical mixture.
- A circuit diagram describes operations, not a time-lapse picture of a particle.
- Counts close to 50/50 are expected, but exact equality is not required.

## Challenge

Predict the output of the modified circuit `qc.x(1)` before running it. Explain the result using amplitudes and probabilities, then restore the controlled-X and verify the correlation.

## AI tutor prompts

- Explain each line of the code and connect it to the circuit diagram.
- Derive the Bell state without skipping the matrix multiplication.
- Explain Qiskit bit ordering using the returned counts.
- Compare a Bell state with a classical correlated mixture.
