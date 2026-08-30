# Quantum Lab API

FastAPI backend for content delivery, Qiskit simulation, restricted classroom code execution, Groq-backed copilot responses, quiz generation, and voice narration endpoints.

## Local commands

```bash
python -m uvicorn app.main:app --reload
python -m compileall app
```

## Core endpoints

- `GET /health`
- `GET /api/v1/status`
- `POST /api/v1/simulation/run`
- `POST /api/v1/simulation/python`
- `POST /api/v1/copilot/chat`
- `POST /api/v1/copilot/quiz`
- `POST /api/v1/voice/text-to-speech`
