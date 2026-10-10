
from datetime import datetime

from pydantic import BaseModel, ConfigDict


class ApplicationCreate(BaseModel):
    resume_filename: str | None = None
    cover_letter: str | None = None


class ApplicationResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    job_id: int
    candidate_id: int
    resume_filename: str | None
    cover_letter: str | None
    status: str
    applied_at: datetime


class ApplicationStatusUpdate(BaseModel):
    status: str
