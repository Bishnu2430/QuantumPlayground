#!/usr/bin/env python3
"""End-to-end backend smoke scenario for local development and CI fallback."""

from __future__ import annotations

import os
import sys
from pathlib import Path
from uuid import uuid4

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "apps" / "api"))

from fastapi.testclient import TestClient

os.environ.setdefault("ENVIRONMENT", "test")
os.environ.setdefault("DATABASE_URL", "sqlite+pysqlite:///./quantum_lab_smoke.db")

from app.main import app  # noqa: E402


def main() -> int:
    suffix = uuid4().hex[:8]
    db_url = os.environ.get("DATABASE_URL", "")
    sqlite_path = Path(db_url.removeprefix("sqlite+pysqlite:///")) if db_url.startswith("sqlite+pysqlite:///") else None
    try:
        if sqlite_path is not None and sqlite_path.exists():
            sqlite_path.unlink()
    except OSError:
        pass
    with TestClient(app) as client:
        assert client.get("/health").status_code == 200
        register = client.post(
            "/api/v1/auth/register",
            json={"email": f"smoke-{suffix}@example.com", "username": f"smoke_{suffix}", "password": "secret1"},
        )
        assert register.status_code == 201, register.text
        login = client.post("/api/v1/auth/login", json={"email": f"smoke-{suffix}@example.com", "password": "secret1"})
        assert login.status_code == 200, login.text
        headers = {"Authorization": f"Bearer {login.json()['access_token']}"}
        circuit = {
            "title": "Bell smoke test",
            "circuit": {
                "numQubits": 2,
                "operations": [
                    {"gate": "h", "targets": [0]},
                    {"gate": "cx", "controls": [0], "targets": [1]},
                    {"gate": "measure", "targets": [0, 1], "clbits": [0, 1]},
                ],
            },
        }
        created = client.post("/api/v1/circuits", json=circuit, headers=headers)
        assert created.status_code == 201, created.text
        run = client.post("/api/v1/simulation/run", json={"circuit": circuit["circuit"], "mode": "shots", "shots": 128}, headers=headers)
        assert run.status_code == 200, run.text
        assert client.get("/api/v1/circuits", headers=headers).status_code == 200
        assert client.get("/api/v1/experiments").status_code == 200
    if sqlite_path is not None:
        sqlite_path.unlink(missing_ok=True)
    print("backend smoke scenario passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
