
from pydantic import BaseModel, ConfigDict, Field


class JobCreate(BaseModel):
    title: str = Field(min_length=2, max_length=150)
    company_name: str = Field(min_length=2, max_length=150)
    location: str | None = None
    job_type: str = "Full-time"
    description: str = Field(min_length=10)
    required_skills: str = Field(min_length=1)
    experience_required: int = Field(default=0, ge=0)
    salary_min: float | None = Field(default=None, ge=0)
    salary_max: float | None = Field(default=None, ge=0)


class JobResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    company_name: str
    location: str | None
    job_type: str | None
    description: str
    required_skills: str
    experience_required: int | None
    salary_min: float | None
    salary_max: float | None
    recruiter_id: int
    is_active: bool
