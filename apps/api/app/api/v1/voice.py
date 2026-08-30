from fastapi import APIRouter

from app.schemas.voice import TextToSpeechRequest, TextToSpeechResponse
from app.services.voice.text_to_speech import synthesize_text

router = APIRouter(tags=["voice"])


@router.post("/text-to-speech", response_model=TextToSpeechResponse)
def text_to_speech(request: TextToSpeechRequest) -> TextToSpeechResponse:
    return synthesize_text(request)
