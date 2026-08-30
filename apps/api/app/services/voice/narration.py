from app.schemas.voice import TextToSpeechRequest, TextToSpeechResponse
from app.services.voice.text_to_speech import synthesize_text


def narrate_lesson(text: str) -> TextToSpeechResponse:
    return synthesize_text(TextToSpeechRequest(text=text, voice="narrator"))
