from typing import Literal

from pydantic import BaseModel, Field

from app.schemas.circuits import QuantumCircuitIR

SimulationMode = Literal["statevector", "shots"]


class SimulationRequest(BaseModel):
    circuit: QuantumCircuitIR
    mode: SimulationMode = "shots"
    shots: int = Field(default=1024, ge=1, le=100_000)
    seed: int | None = 42


class SimulationResult(BaseModel):
    backend: str
    numQubits: int
    shots: int | None = None
    counts: dict[str, int] | None = None
    probabilities: dict[str, float] | None = None
    statevector: list[dict[str, float]] | None = None
    durationMs: int
    metadata: dict = Field(default_factory=dict)
