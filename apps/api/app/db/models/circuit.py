from typing import Optional

from sqlalchemy import String, Text, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.database import Base
from app.db.models import UUIDMixin, TimestampMixin


class Circuit(UUIDMixin, TimestampMixin, Base):
    """Circuit model for user-created quantum circuits."""

    __tablename__ = "circuits"

    owner_id: Mapped[str] = mapped_column(String(36), ForeignKey("users.id"), nullable=False, index=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    ir_json: Mapped[str] = mapped_column(Text, nullable=False)  # Quantum IR as JSON
    num_qubits: Mapped[int] = mapped_column(Integer, nullable=False)
    is_public: Mapped[bool] = mapped_column(default=False, nullable=False)
    related_lesson_id: Mapped[Optional[str]] = mapped_column(
        String(36), ForeignKey("lessons.id"), nullable=True
    )

    # Relationships
    owner = relationship("User", back_populates="circuits")
    versions = relationship(
        "CircuitVersion", back_populates="circuit", cascade="all, delete-orphan"
    )
    simulation_runs = relationship(
        "SimulationRun", back_populates="circuit", cascade="all, delete-orphan"
    )


class CircuitVersion(UUIDMixin, TimestampMixin, Base):
    """Versioned snapshots of circuits for undo/history."""

    __tablename__ = "circuit_versions"

    circuit_id: Mapped[str] = mapped_column(String(36), ForeignKey("circuits.id"), nullable=False, index=True)
    version_number: Mapped[int] = mapped_column(Integer, nullable=False)
    ir_json: Mapped[str] = mapped_column(Text, nullable=False)
    change_summary: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    # Relationships
    circuit = relationship("Circuit", back_populates="versions")
