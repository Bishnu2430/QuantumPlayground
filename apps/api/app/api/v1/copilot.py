from fastapi import APIRouter

from app.schemas.ai import CopilotRequest, CopilotResponse, QuizRequest, QuizResponse
from app.services.ai.agent import QuantumCopilotAgent

router = APIRouter(tags=["copilot"])


@router.post("/chat", response_model=CopilotResponse)
def chat(request: CopilotRequest) -> CopilotResponse:
    return QuantumCopilotAgent().answer(request)


@router.post("/quiz", response_model=QuizResponse)
def quiz(request: QuizRequest) -> QuizResponse:
    return QuantumCopilotAgent().quiz(request)
