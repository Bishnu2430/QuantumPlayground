from typing import Optional

from sqlalchemy import String, Integer, Float, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.database import Base
from app.db.models import UUIDMixin, TimestampMixin


class Progress(UUIDMixin, TimestampMixin, Base):
    """User progress tracking for lessons and concepts."""

    __tablename__ = "progress"

    user_id: Mapped[str] = mapped_column(String(36), ForeignKey("users.id"), nullable=False, index=True)
    lesson_id: Mapped[str] = mapped_column(String(36), ForeignKey("lessons.id"), nullable=False, index=True)
    is_completed: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    is_started: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    mastery_level: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)  # 0.0 to 1.0
    attempts: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    time_spent_seconds: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    last_attempted_at: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)

    # Relationships
    user = relationship("User", back_populates="progress_records")
    lesson = relationship("Lesson", back_populates="progress_records")
