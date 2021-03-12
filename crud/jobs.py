from typing import List

from sqlalchemy.orm import Session

from models.jobs import Job as mJob
from schemas.jobs import Job as sJob


async def select_by_id(db: Session, job_id: int) -> mJob:
    return await db.query(mJob).filter(mJob.id == job_id).first()


async def get_all(db: Session, skip: int = 0, limit: int = 100) -> List[mJob]:
    return db.query(mJob).offset(skip).limit(limit).all()


async def create(db: Session, job: sJob) -> mJob:
    db_job = mJob(
        title=job.title,
        company=job.company,
        achievements=job.achievements
    )
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return await db_job


async def update(db: Session, job_id: int, job: mJob) -> mJob:
    return await select_by_id(db, job_id)
