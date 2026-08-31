from app.schemas.voice import TextToSpeechRequest, TextToSpeechResponse
from app.services.voice.text_to_speech import synthesize_text


def run_tts_job(request: TextToSpeechRequest) -> TextToSpeechResponse:
    return synthesize_text(request)
