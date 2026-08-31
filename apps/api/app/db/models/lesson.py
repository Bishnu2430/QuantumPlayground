from typing import Optional

from sqlalchemy import String, Text, Integer, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.database import Base
from app.db.models import UUIDMixin, TimestampMixin


class Lesson(UUIDMixin, TimestampMixin, Base):
    """Lesson model for curriculum content."""

    __tablename__ = "lessons"

    slug: Mapped[str] = mapped_column(String(255), unique=True, nullable=False, index=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    difficulty: Mapped[int] = mapped_column(Integer, default=1, nullable=False)  # 1-5
    domain: Mapped[str] = mapped_column(String(255), nullable=False, index=True)  # e.g., "introduction"
    module: Mapped[str] = mapped_column(String(255), nullable=False, index=True)  # e.g., "what-is-computation"
    order: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    is_published: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    prerequisites: Mapped[Optional[str]] = mapped_column(Text, nullable=True)  # JSON array of lesson slugs

    # Relationships
    progress_records = relationship(
        "Progress", back_populates="lesson", cascade="all, delete-orphan"
    )
