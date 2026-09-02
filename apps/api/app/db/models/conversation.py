from typing import Optional

from sqlalchemy import String, Text, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.database import Base
from app.db.models import UUIDMixin, TimestampMixin


class Conversation(UUIDMixin, TimestampMixin, Base):
    """AI conversation history."""

    __tablename__ = "conversations"

    user_id: Mapped[str] = mapped_column(String(36), ForeignKey("users.id"), nullable=False, index=True)
    title: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    context_lesson_id: Mapped[Optional[str]] = mapped_column(String(36), ForeignKey("lessons.id"), nullable=True)
    context_circuit_id: Mapped[Optional[str]] = mapped_column(String(36), ForeignKey("circuits.id"), nullable=True)
    message_count: Mapped[int] = mapped_column(Integer, default=0, nullable=False)

    # Relationships
    user = relationship("User", back_populates="conversations")
    messages = relationship("Message", back_populates="conversation", cascade="all, delete-orphan")


class Message(UUIDMixin, TimestampMixin, Base):
    """Individual messages in a conversation."""

    __tablename__ = "messages"

    conversation_id: Mapped[str] = mapped_column(
        String(36), ForeignKey("conversations.id"), nullable=False, index=True
    )
    role: Mapped[str] = mapped_column(String(50), nullable=False)  # "user" or "assistant"
    content: Mapped[str] = mapped_column(Text, nullable=False)
    message_metadata: Mapped[Optional[str]] = mapped_column("metadata", Text, nullable=True)  # JSON metadata

    # Relationships
    conversation = relationship("Conversation", back_populates="messages")
