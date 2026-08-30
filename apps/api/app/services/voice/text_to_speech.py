from app.schemas.voice import TextToSpeechRequest, TextToSpeechResponse


def synthesize_text(request: TextToSpeechRequest) -> TextToSpeechResponse:
    return TextToSpeechResponse(transcript=request.text)
