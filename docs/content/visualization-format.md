# Visualization Format

## 1. Goal

A visualization is a reusable teaching asset that can be driven by lesson state, circuit state, simulation output, or a narration timeline.

## 2. Metadata schema

Example:

```yaml
id: viz_bloch_hadamard
kind: blochSphere
title: Hadamard on a Qubit
inputs:
  - statevector
  - operation
controls:
  - theta
  - phi
  - autoplay
interactions:
  - rotateCamera
  - applyGate
  - reset
accessibility:
  description: "A Bloch sphere showing the state vector..."
assets:
  - /visualizations/bloch/default.json
```

## 3. Visualization kinds

Examples:

- `blochSphere`
- `stateVector`
- `probabilityBars`
- `histogram`
- `densityMatrix`
- `circuitTimeline`
- `interference`
- `quantumNetwork`
- `hardwareTopology`
- `algorithmAnimation`
- `timeline`

## 4. Event model

Visualizations can listen to normalized events:

```text
gate_applied
state_changed
measurement_started
measurement_completed
simulation_completed
lesson_step_changed
narration_started
narration_ended
```

## 5. Data separation

Keep scientific state separate from rendering state. Example:

```text
Scientific data
  statevector = [...]
  probabilities = {...}

Rendering state
  cameraPosition
  highlightedQubit
  animationProgress
```

This allows the same simulation output to drive multiple visualizations.

## 6. 3D principles

- Show only the information that helps the learner.
- Label axes and basis states clearly.
- Provide a reset/home camera control.
- Offer a reduced-motion alternative.
- Never make a purely decorative 3D effect imply a scientifically false physical process.

## 7. Pre-staged animation support

Large or deterministic explanatory scenes can be pre-staged as video or animation assets. Interactive controls should remain live where educational value depends on learner input.
