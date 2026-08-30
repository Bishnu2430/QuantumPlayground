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
