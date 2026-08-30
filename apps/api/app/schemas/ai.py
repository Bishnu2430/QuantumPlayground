from typing import Literal

from pydantic import BaseModel, Field

from app.schemas.circuits import QuantumCircuitIR
from app.schemas.simulations import SimulationResult

Depth = Literal["intuitive", "undergraduate", "mathematical", "formal"]


class CopilotContext(BaseModel):
    lessonId: str | None = None
    selectedText: str | None = None
    circuit: QuantumCircuitIR | None = None
    latestResult: SimulationResult | None = None
    code: str | None = None


class CopilotRequest(BaseModel):
    message: str = Field(min_length=1, max_length=8_000)
    depth: Depth = "undergraduate"
    context: CopilotContext = Field(default_factory=CopilotContext)


class CopilotResponse(BaseModel):
    answer: str
    model: str
    toolCalls: list[str] = Field(default_factory=list)
    citations: list[str] = Field(default_factory=list)


class QuizRequest(BaseModel):
    topic: str = Field(min_length=1, max_length=200)
    difficulty: Depth = "undergraduate"
    includeCode: bool = False


class QuizQuestion(BaseModel):
    prompt: str
    choices: list[str]
    answerIndex: int
    explanation: str
    code: str | None = None


class QuizResponse(BaseModel):
    topic: str
    questions: list[QuizQuestion]
