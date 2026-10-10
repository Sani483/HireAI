
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.api.dependencies import get_db, get_current_user
from app.models import Application, Job, User
from app.schemas import (
    ApplicationCreate,
    ApplicationResponse,
    ApplicationStatusUpdate,
)

router = APIRouter(
    prefix="/api/applications",
    tags=["Applications"]
)

ALLOWED_STATUSES = {
    "applied", "reviewing", "shortlisted", "rejected", "hired"
}


@router.post("/{job_id}", response_model=ApplicationResponse,
             status_code=201)
def apply_for_job(
    job_id: int,
    data: ApplicationCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    if current_user.role != "candidate":
        raise HTTPException(
            status_code=403,
            detail="Only candidates can apply for jobs"
        )

    job = db.query(Job).filter(
        Job.id == job_id,
        Job.is_active.is_(True)
    ).first()

    if job is None:
        raise HTTPException(status_code=404, detail="Job not found")

    existing = db.query(Application).filter(
        Application.job_id == job_id,
        Application.candidate_id == current_user.id
    ).first()

    if existing:
        raise HTTPException(
            status_code=409,
            detail="You have already applied for this job"
        )

    application = Application(
        job_id=job_id,
        candidate_id=current_user.id,
        resume_filename=data.resume_filename,
        cover_letter=data.cover_letter,
        status="applied",
    )

    db.add(application)

    try:
        db.commit()
        db.refresh(application)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail="Application already exists"
        )

    return application


@router.get("/my", response_model=list[ApplicationResponse])
def my_applications(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    if current_user.role != "candidate":
        raise HTTPException(
            status_code=403,
            detail="Only candidates can view their applications"
        )

    return (
        db.query(Application)
        .filter(Application.candidate_id == current_user.id)
        .order_by(Application.applied_at.desc())
        .all()
    )


@router.get("/job/{job_id}", response_model=list[ApplicationResponse])
def applications_for_job(
    job_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    if current_user.role != "recruiter":
        raise HTTPException(
            status_code=403,
            detail="Only recruiters can view job applications"
        )

    job = db.query(Job).filter(
        Job.id == job_id,
        Job.recruiter_id == current_user.id
    ).first()

    if job is None:
        raise HTTPException(
            status_code=404,
            detail="Job not found for this recruiter"
        )

    return (
        db.query(Application)
        .filter(Application.job_id == job_id)
        .order_by(Application.applied_at.desc())
        .all()
    )


@router.patch("/{application_id}/status",
              response_model=ApplicationResponse)
def update_application_status(
    application_id: int,
    data: ApplicationStatusUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    if current_user.role != "recruiter":
        raise HTTPException(
            status_code=403,
            detail="Only recruiters can update application status"
        )

    if data.status not in ALLOWED_STATUSES:
        raise HTTPException(
            status_code=422,
            detail="Invalid application status"
        )

    application = db.query(Application).filter(
        Application.id == application_id
    ).first()

    if application is None:
        raise HTTPException(
            status_code=404,
            detail="Application not found"
        )

    job = db.query(Job).filter(
        Job.id == application.job_id,
        Job.recruiter_id == current_user.id
    ).first()

    if job is None:
        raise HTTPException(
            status_code=403,
            detail="You cannot manage this application"
        )

    application.status = data.status
    db.commit()
    db.refresh(application)

    return application
