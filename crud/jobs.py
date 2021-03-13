from typing import List

from sqlalchemy.orm import Session

from models.jobs import Job as mJob
from schemas.jobs import Job as sJob


def select_by_id(db: Session, job_id: int) -> mJob:
    return db.query(mJob).filter(mJob.id == job_id).first()


def get_all(db: Session, skip: int = 0, limit: int = 100) -> List[mJob]:
    return db.query(mJob).offset(skip).limit(limit).all()


def create(db: Session, job: sJob) -> mJob:
    db_job = mJob(
        title=job.title,
        company=job.company,
        achievements=job.achievements
    )
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job


def update(db: Session, job_id: int, job: mJob) -> mJob:
    return select_by_id(db, job_id)
