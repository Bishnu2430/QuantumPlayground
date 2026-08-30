from typing import Literal

from pydantic import BaseModel, Field, model_validator

GateName = Literal[
    "id",
    "x",
    "y",
    "z",
    "h",
    "s",
    "sdg",
    "t",
    "tdg",
    "rx",
    "ry",
    "rz",
    "cx",
    "cz",
    "swap",
    "measure",
]


class CircuitOperation(BaseModel):
    gate: GateName
    targets: list[int] = Field(default_factory=list)
    controls: list[int] = Field(default_factory=list)
    clbits: list[int] = Field(default_factory=list)
    params: list[float] = Field(default_factory=list)
    moment: int = 0


class QuantumCircuitIR(BaseModel):
    numQubits: int = Field(ge=1, le=32)
    numClbits: int = Field(default=0, ge=0, le=32)
    operations: list[CircuitOperation] = Field(default_factory=list)

    @model_validator(mode="after")
    def default_classical_bits(self) -> "QuantumCircuitIR":
        if self.numClbits == 0 and any(op.gate == "measure" for op in self.operations):
            self.numClbits = self.numQubits
        return self


class CodeRunRequest(BaseModel):
    code: str = Field(min_length=1, max_length=20_000)
    timeoutSeconds: int | None = Field(default=None, ge=1, le=30)
