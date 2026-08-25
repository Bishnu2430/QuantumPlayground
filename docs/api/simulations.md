# Simulations API

**Base path:** `/api/v1/simulations`

## 1. Modes

- `statevector`
- `shots`
- `noise`

Hardware execution can later use the same job model with a provider-specific backend type.

## 2. Synchronous execution

For small educational circuits:

### `POST /run`

Request:

```json
{
  "circuitId": "c_123",
  "mode": "shots",
  "shots": 1024,
  "noiseModel": null
}
```

Response contains normalized counts, probabilities, metadata, and timing.

## 3. Asynchronous execution

### `POST /jobs`

Returns:

```json
{
  "jobId": "job_123",
  "status": "queued"
}
```

### `GET /jobs/{jobId}`

Returns `queued`, `running`, `completed`, `failed`, or `cancelled`.

## 4. Result contract

```json
{
  "jobId": "job_123",
  "backend": "qiskit-aer",
  "numQubits": 2,
  "shots": 1024,
  "counts": {"00": 506, "11": 518},
  "probabilities": {"00": 0.4941, "11": 0.5059},
  "durationMs": 29
}
```

Statevector output should only be returned when requested and within configured size limits.

## 5. Resource limits

Every request is constrained by circuit size, shots, execution time, and output size. Limits can differ between anonymous users and authenticated users.
