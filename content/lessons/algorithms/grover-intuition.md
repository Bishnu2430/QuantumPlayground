---
id: grover-intuition
type: algorithm
domain: algorithms
title: Grover Search — Intuition
summary: "Amplitude amplification gives a quadratic query speedup for unstructured search."
level: advanced
prerequisites: [superposition, phase-kickback, reflection]
tags: [grover, search, amplitude-amplification]
equations: [grover-iteration, grover-complexity]
visualizations: [grover-geometry]
experiments: [grover-2-qubits]
references: [nielsen-chuang, gentle-introduction]
---

# Grover Search — Intuition

Suppose there are $N$ equally likely candidates and an oracle marks one or more solutions. Classical black-box search requires a number of queries proportional to $N$ in the worst case. Grover's algorithm reaches the marked subspace using a number of oracle calls proportional to $\sqrt N$.

## The four-step loop

1. Prepare a uniform superposition.
2. Apply an oracle that flips the phase of marked states.
3. Reflect amplitudes about their mean (the diffusion step).
4. Repeat approximately $\pi\sqrt N/4$ times for one marked item.

## The geometric picture

The useful dynamics live in a two-dimensional subspace: one axis represents the normalized marked subspace and the other the normalized unmarked subspace. Each iteration rotates the state toward the marked axis.

## What the demo should show

- current iteration number;
- marked amplitude;
- unmarked amplitude;
- success probability;
- optimal iteration estimate;
- the point where further iterations begin to decrease success probability.

## Challenge

For a four-item database with one marked state, predict the best number of iterations before running the circuit. Then change the marked state and verify that the structure, not the label, determines the result.
