# Users and Progress API

**Base path:** `/api/v1/users`

## 1. Profile

### `GET /me`

Return profile and high-level progress.

### `PATCH /me`

Update editable profile preferences such as display name, learning depth, and narration settings.

## 2. Learning progress

### `GET /me/progress`

Returns completed lessons, concept mastery, recent experiments, and assessments.

### `GET /me/skills`

Returns normalized skill scores, for example:

```json
{
  "qubits": 0.84,
  "measurement": 0.71,
  "entanglement": 0.52,
  "grover": 0.37
}
```

Scores are internal learning signals, not objective measures of a person's scientific ability.

## 3. Recommendations

### `GET /me/recommendations`

Returns the next lessons or experiments based on prerequisites, activity, and mastery signals.

## 4. Privacy

Provide endpoints or account flows for:

- export of personal data;
- deletion of account data;
- conversation deletion;
- progress deletion where product policy permits.

## 5. Instructor extension

Instructor APIs should be placed under a separate role-protected namespace, for example `/api/v1/instructor/...`, rather than exposing student analytics to all authenticated users.
