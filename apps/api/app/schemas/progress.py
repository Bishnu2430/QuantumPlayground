from pydantic import BaseModel, Field


class ProgressResponse(BaseModel):
    """User progress response."""

    id: str
    user_id: str
    lesson_id: str
    is_completed: bool
    is_started: bool
    mastery_level: float
    attempts: int
    time_spent_seconds: int
    created_at: str
    updated_at: str

    class Config:
        from_attributes = True


class ProgressUpdate(BaseModel):
    """Progress update request."""

    is_started: bool | None = None
    is_completed: bool | None = None
    mastery_level: float | None = Field(None, ge=0.0, le=1.0)
    attempts: int | None = None
    time_spent_seconds: int | None = None
