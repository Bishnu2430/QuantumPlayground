# Content Schema

**Status:** Draft baseline  
**Format:** Markdown/MDX content + structured YAML/JSON metadata

## 1. Philosophy

Content should be stored as composable educational objects. A lesson is an assembly of reusable blocks rather than one giant document.

## 2. Lesson metadata

Example:

```yaml
id: lesson_superposition
slug: superposition
title: Superposition
difficulty: beginner
estimatedMinutes: 20
tags:
  - qubit
  - amplitudes
prerequisites:
  - qubit
learningObjectives:
  - explain superposition qualitatively
  - normalize a single-qubit state
  - predict H|0>
sections:
  - id: intuition
    type: markdown
  - id: math
    type: equation
  - id: bloch
    type: visualization
  - id: experiment
    type: experiment
  - id: code
    type: code
  - id: challenge
    type: assessment
references:
  - ref_superposition_01
```

## 3. Block types

Supported conceptual types:

- `markdown`
- `equation`
- `image`
- `video`
- `visualization`
- `simulation`
- `code`
- `circuit`
- `experiment`
- `assessment`
- `callout`
- `timeline`
- `reference`

## 4. Concepts and prerequisites

Concepts should be atomic and graph-addressable. Example:

```yaml
id: concept_hadamard
prerequisites:
  - qubit
  - basis_state
related:
  - superposition
  - interference
```

This graph powers recommendations and AI context.

## 5. Scientific references

Every formal or empirical claim should be traceable to one or more references. Reference metadata should include author, title, publication date, URL/identifier, license/usage note, and exact location such as page, section, or chapter when available.

## 6. Content validation

CI should validate:

- unique IDs and slugs;
- valid prerequisite references;
- valid visualization IDs;
- valid experiment IDs;
- required learning objectives;
- broken asset references;
- missing citations for content types that require them.
