from typing import Optional

from pydantic import BaseModel, Field


class LessonResponse(BaseModel):
    """Lesson data response."""

    id: str
    slug: str
    title: str
    description: Optional[str]
    content: str
    difficulty: int
    domain: str
    module: str
    order: int
    is_published: bool
    prerequisites: Optional[str]
    created_at: str
    updated_at: str

    class Config:
        from_attributes = True


class LessonCreate(BaseModel):
    """Lesson creation request."""

    slug: str = Field(min_length=1, max_length=255)
    title: str = Field(min_length=1, max_length=255)
    description: Optional[str] = None
    content: str = Field(min_length=1)
    difficulty: int = Field(ge=1, le=5)
    domain: str = Field(min_length=1, max_length=255)
    module: str = Field(min_length=1, max_length=255)
    order: int = 0
    is_published: bool = False
    prerequisites: Optional[str] = None


class LessonUpdate(BaseModel):
    """Lesson update request."""

    title: Optional[str] = None
    description: Optional[str] = None
    content: Optional[str] = None
    difficulty: Optional[int] = None
    is_published: Optional[bool] = None
