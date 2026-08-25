# Lessons API

**Base path:** `/api/v1/lessons`

## 1. Lesson model

A lesson combines theory, mathematics, visualization, experiments, code, assessments, and references.

## 2. Endpoints

### `GET /`

List published lessons with filters such as topic, difficulty, and prerequisite state.

### `GET /{slug}`

Return the complete lesson metadata and content references.

### `GET /{slug}/experiments`

Return experiments embedded in or associated with the lesson.

### `GET /{slug}/assessment`

Return assessment items appropriate for the lesson.

### `POST /{slug}/complete`

Record lesson completion after required activities have been satisfied.

### `GET /{slug}/progress`

Return the current learner's progress for the lesson.

## 3. Content response

The API should expose structured content rather than raw filesystem paths.

Example:

```json
{
  "slug": "superposition",
  "title": "Superposition",
  "difficulty": "beginner",
  "prerequisites": ["qubit"],
  "sections": [
    {"type": "markdown", "ref": "..."},
    {"type": "equation", "ref": "..."},
    {"type": "visualization", "ref": "..."},
    {"type": "experiment", "ref": "..."},
    {"type": "code", "language": "python", "source": "..."}
  ]
}
```

## 4. Versioning

Published lessons are immutable by default. Edits create a new content version so historical learner attempts remain reproducible.
