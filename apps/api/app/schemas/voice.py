from pydantic import BaseModel, Field


class TextToSpeechRequest(BaseModel):
    text: str = Field(min_length=1, max_length=4_000)
    voice: str = "default"


class TextToSpeechResponse(BaseModel):
    audioUrl: str | None = None
    transcript: str
    format: str = "text-placeholder"
