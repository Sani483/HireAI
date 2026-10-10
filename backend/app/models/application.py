
from datetime import datetime

from sqlalchemy import (
    CheckConstraint,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Text,
    UniqueConstraint,
)
from sqlalchemy.orm import Mapped, mapped_column

from app.database.connection import Base


class Application(Base):
    __tablename__ = "applications"

    __table_args__ = (
        UniqueConstraint(
            "job_id", "candidate_id",
            name="unique_candidate_job"
        ),
        CheckConstraint(
            "status IN ('applied', 'reviewing', 'shortlisted', 'rejected', 'hired')",
            name="valid_application_status"
        ),
    )

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, index=True
    )
    job_id: Mapped[int] = mapped_column(
        ForeignKey("jobs.id"), nullable=False
    )
    candidate_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"), nullable=False
    )
    resume_filename: Mapped[str | None] = mapped_column(
        String(255)
    )
    cover_letter: Mapped[str | None] = mapped_column(Text)
    status: Mapped[str] = mapped_column(
        String(30), default="applied", nullable=False
    )
    applied_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, nullable=False
    )
