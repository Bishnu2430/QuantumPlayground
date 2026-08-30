---
id: teleportation
type: algorithm
domain: entanglement
title: Quantum Teleportation
summary: "Transfer an unknown qubit state using a shared entangled pair and two classical bits."
level: advanced
prerequisites: [bell-states, measurement, cnot, classical-conditions]
tags: [teleportation, entanglement, protocol]
equations: [teleportation-identity]
visualizations: [teleportation-timeline]
experiments: [teleportation]
references: [nielsen-chuang]
---

# Quantum Teleportation

Quantum teleportation transfers an **unknown quantum state** from Alice to Bob. The protocol needs a pre-shared Bell pair and two classical measurement bits. No energy or matter is teleported, and the protocol does not transmit usable information faster than light.

## State-level derivation

Let

$$|\psi\rangle = \alpha|0\rangle+\beta|1\rangle.$$

Alice and Bob share

$$|\Phi^+\rangle = (|00\rangle+|11\rangle)/\sqrt2.$$

The three-qubit state can be regrouped in the Bell basis of Alice's two qubits:

$$|\psi\rangle|\Phi^+\rangle = \frac12\left(|\Phi^+\rangle|\psi\rangle + |\Phi^-\rangle Z|\psi\rangle + |\Psi^+\rangle X|\psi\rangle + |\Psi^-\rangle XZ|\psi\rangle\right).$$

Alice's measurement selects one term. Her two classical bits tell Bob which Pauli correction to apply.

## Why no-cloning is preserved

Alice's measurement destroys the original usable state at her location. Bob reconstructs the state conditionally; a second independent copy is not produced.

## Visual timeline

The visualization should show entanglement creation, Bell measurement, classical communication and correction as distinct layers. The classical channel must be visually different from the quantum wires.

## Challenge

Change the input state to several points on the Bloch sphere. Verify that the final Bob state matches the input state up to numerical precision.
