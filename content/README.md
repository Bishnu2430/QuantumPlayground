# Quantum Lab Content

This directory is the source-of-truth for Quantum Lab's educational content.

## Content philosophy

Every important idea is represented across five layers:

1. **Intuition** — plain-language mental model.
2. **Formalism** — physics/mathematical statement.
3. **Visualization** — a dynamic 2D/3D representation.
4. **Experiment** — an executable interaction or Qiskit circuit.
5. **Challenge** — a task that requires the learner to predict, construct,
   debug, or explain.

The AI tutor should retrieve these layers independently so that one learner can
ask for a one-minute explanation while another asks for a derivation or a code
review of the same concept.

## Source and citation policy

Reference metadata is stored in `references/sources.yaml`. Do not commit
copyrighted full-text book scans or other unauthorized copies. Build the corpus
from sources that are public-domain, open-licensed, appropriately licensed,
official documentation, or otherwise legally usable.

## Directory map

- `curriculum/` — ordered domains, modules and lesson IDs.
- `lessons/` — authored lesson pages.
- `equations/` — reusable mathematical definitions/derivations.
- `experiments/` — executable learning activities.
- `visualizations/` — declarative scenes and animation timelines.
- `challenges/` — assessment/coding/debugging tasks.
- `glossary/` — terminology and pronunciation metadata.
- `media/` — asset metadata and future images/video/audio/3D files.
- `assessment/` — rubrics and mastery configuration.
- `ai/` — AI tutoring policy and retrieval metadata.
- `references/` — bibliographic/source metadata.

## Lesson authoring contract

Every lesson should answer the same learning loop: predict, derive, build, run,
inspect, and explain. Keep the frontmatter `domain`, `equations`,
`visualizations`, `experiments`, and `references` IDs valid so the application
can assemble the lesson page and its interactive tools without hard-coded
knowledge of a topic.

Use these sections in order:

1. `What this means` — a precise plain-language claim and its scope.
2. `Build the intuition` — a mental model with an explicit limitation.
3. `Formal statement` — notation, assumptions, and normalization conditions.
4. `Mathematical lens` — intermediate algebra, not an unexplained conclusion.
5. `Visual lens` — name the observable quantity and how it changes.
6. `Experiment` — prediction, executable setup, expected result, and a perturbation.
7. `Code example` — a small Qiskit example that runs in the classroom sandbox.
8. `Common misconceptions`, `Challenge`, and `AI tutor prompts`.

Visual specifications are declarative. Use `equation` for derivations,
`graph` for measured data, `circuit` for Quantum IR, `scene3d` for Bloch or
physical scenes, and `codeRunner` for executable notebooks. The frontend must
label ideal predictions separately from sampled or noisy results.

The current software references are IBM Quantum's [first circuit guide](https://quantum.cloud.ibm.com/docs/en/guides/hello-world),
[Aer simulation guide](https://quantum.cloud.ibm.com/docs/en/guides/simulate-with-qiskit-aer),
and [circuit visualization guide](https://quantum.cloud.ibm.com/docs/en/guides/visualize-circuits).
