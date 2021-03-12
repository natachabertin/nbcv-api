from typing import List

from sqlalchemy.orm import Session

from models.jobs import Job as mJob
from schemas.jobs import Job as sJob


async def select_by_id(db: Session, ed_id: int) -> mJob:
    return await db.query(mJob).filter(mJob.id == ed_id).first()


async def get_all(db: Session, skip: int = 0, limit: int = 100) -> List[mJob]:
    return db.query(mJob).offset(skip).limit(limit).all()


async def create(db: Session, jobs: sJob) -> mJob:
    db_ed = mJob(
        title=jobs.title,
        company=jobs.company,
        achievements=jobs.achievements
    )
    db.add(db_ed)
    db.commit()
    db.refresh(db_ed)
    return await db_ed


async def update(db: Session, ed_id: int, jobs: mJob) -> mJob:
    return await select_by_id(ed_id)

