from typing import Optional

from sqlalchemy import String, Text, Integer, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.database import Base
from app.db.models import UUIDMixin, TimestampMixin


class SimulationRun(UUIDMixin, TimestampMixin, Base):
    """Record of a quantum simulation execution."""

    __tablename__ = "simulation_runs"

    user_id: Mapped[str] = mapped_column(String(36), ForeignKey("users.id"), nullable=False, index=True)
    circuit_id: Mapped[str] = mapped_column(String(36), ForeignKey("circuits.id"), nullable=False, index=True)
    backend: Mapped[str] = mapped_column(String(255), nullable=False)  # e.g., "qiskit-aer"
    mode: Mapped[str] = mapped_column(String(50), nullable=False)  # "statevector" or "shots"
    shots: Mapped[int] = mapped_column(Integer, default=1024, nullable=False)
    seed: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    status: Mapped[str] = mapped_column(String(50), default="completed", nullable=False)  # "pending", "running", "completed", "failed"
    result_json: Mapped[Optional[str]] = mapped_column(Text, nullable=True)  # Simulation result as JSON
    error_message: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    duration_ms: Mapped[int] = mapped_column(Integer, default=0, nullable=False)

    # Relationships
    user = relationship("User", back_populates="simulation_runs")
    circuit = relationship("Circuit", back_populates="simulation_runs")
