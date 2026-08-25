# Circuits API

**Base path:** `/api/v1/circuits`

## 1. Canonical representation

The API accepts and returns the platform's Quantum IR, not raw Qiskit objects.

## 2. Endpoints

### `POST /`

Create a circuit.

### `GET /`

List the authenticated user's circuits.

### `GET /{id}`

Return circuit metadata and current IR.

### `PUT /{id}`

Replace current circuit state with a validated IR document.

### `POST /{id}/versions`

Create a named immutable version/snapshot.

### `GET /{id}/versions`

List historical circuit versions.

### `DELETE /{id}`

Delete a user-owned circuit subject to retention policy.

## 3. AI modification flow

AI should never silently mutate a circuit. The AI service returns structured operations or a proposed replacement IR. The frontend displays a diff/preview and the user accepts the change.

## 4. Example

```json
{
  "numQubits": 2,
  "numClbits": 2,
  "operations": [
    {"gate": "h", "targets": [0], "moment": 0},
    {"gate": "cx", "controls": [0], "targets": [1], "moment": 1}
  ]
}
```

## 5. Validation

A malformed or unsupported operation returns a structured validation error and does not overwrite the previous valid circuit.
