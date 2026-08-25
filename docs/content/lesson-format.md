# Lesson Format

## 1. Lesson teaching pattern

The preferred structure is:

`Question → Intuition → Formalism → Visualization → Experiment → Code → Reflection → Challenge`

Not every lesson needs every block, but the platform should encourage a multi-modal representation of important concepts.

## 2. Recommended lesson anatomy

### 1. Hook

A surprising question, visual, or experiment.

### 2. Intuition

Explain the concept without unnecessary notation.

### 3. Mathematics

Introduce equations and derive the important result.

### 4. Visualization

Show the same concept as a diagram, animation, 3D object, or interactive chart.

### 5. Experiment

Let the learner change a parameter and predict what will happen.

### 6. Code

Show a minimal Qiskit example.

### 7. Simulation

Run the example and visualize the actual output.

### 8. AI conversation

Invite the learner to ask questions about the current experiment.

### 9. Challenge

Ask the learner to construct, derive, debug, or predict something without directly revealing the answer.

## 3. Difficulty levels

Use four levels:

- `beginner`
- `intermediate`
- `advanced`
- `formal`

Difficulty describes prerequisite knowledge, not intellectual value.

## 4. Content quality standard

A concept should ideally provide:

- precise definition;
- intuitive explanation;
- equations where meaningful;
- at least one visualization;
- at least one experiment or code example for computational concepts;
- references;
- common misconceptions;
- one challenge or reflection question.

## 5. Voice-ready lessons

Narration should be authored as short segments rather than one long paragraph. Each segment should optionally reference a visual action so audio and simulation can stay synchronized.

Example:

```yaml
- id: narration_01
  text: "The Hadamard gate creates an equal superposition."
  visualAction: "apply_hadamard"
- id: narration_02
  text: "The Bloch vector moves from the north pole to the equator."
  visualAction: "rotate_bloch_vector"
```

## 6. Assessment principles

Prefer prediction, construction, debugging, and explanation over recall-only questions. Example:

> Predict the measurement distribution before running the circuit.

Then let the learner compare the prediction with the actual result.
