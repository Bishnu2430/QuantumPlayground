from groq import Groq

from app.core.config import Settings, get_settings
from app.schemas.ai import CopilotRequest, CopilotResponse, QuizQuestion, QuizRequest, QuizResponse
from app.services.ai.prompts import SYSTEM_PROMPT


def _context_summary(request: CopilotRequest) -> str:
    context = request.context
    parts = [f"Depth: {request.depth}"]
    if context.lessonId:
        parts.append(f"Lesson: {context.lessonId}")
    if context.selectedText:
        parts.append(f"Selected text: {context.selectedText}")
    if context.circuit:
        parts.append(f"Circuit IR: {context.circuit.model_dump_json()}")
    if context.latestResult:
        parts.append(f"Latest result: {context.latestResult.model_dump_json()}")
    if context.code:
        parts.append(f"Code under discussion:\n{context.code}")
    return "\n".join(parts)


class QuantumCopilotAgent:
    def __init__(self, settings: Settings | None = None) -> None:
        self.settings = settings or get_settings()
        self.client = Groq(api_key=self.settings.groq_api_key) if self.settings.groq_api_key else None

    def answer(self, request: CopilotRequest) -> CopilotResponse:
        if self.client is None:
            return CopilotResponse(
                answer="Groq is not configured. I can still inspect supplied context once GROQ_API_KEY is available.",
                model="offline",
            )
        completion = self.client.chat.completions.create(
            model=self.settings.groq_model,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": f"{_context_summary(request)}\n\nQuestion: {request.message}"},
            ],
            temperature=0.2,
        )
        answer = completion.choices[0].message.content or "I could not generate an answer."
        return CopilotResponse(answer=answer, model=self.settings.groq_model)

    def quiz(self, request: QuizRequest) -> QuizResponse:
        code = None
        if request.includeCode:
            code = "from qiskit import QuantumCircuit\nqc = QuantumCircuit(1, 1)\nqc.h(0)\nqc.measure(0, 0)\nprint(qc)"
        return QuizResponse(
            topic=request.topic,
            questions=[
                QuizQuestion(
                    prompt=f"For {request.topic}, what should a valid Quantum Lab answer rely on when numerical behavior matters?",
                    choices=["A deterministic simulator/tool result", "A guessed LLM value", "Only visual intuition", "A random historical anecdote"],
                    answerIndex=0,
                    explanation="Quantum Lab treats simulator output as authoritative for numerical quantum behavior.",
                    code=code,
                )
            ],
        )
