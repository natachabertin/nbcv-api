from typing import List

from sqlalchemy.orm import Session

from crud.base import select_item_by_id, list_items, create_item, update_item
from models.jobs import Job as mJob
from schemas.jobs import Job as sJob


def select_by_id(db: Session, job_id: int) -> mJob:
    return select_item_by_id(db, mJob, job_id)


def get_all(db: Session, skip: int = 0, limit: int = 100) -> List[mJob]:
    return list_items(db, mJob, skip, limit)


def create(db: Session, job: sJob) -> mJob:
    return create_item(db, job, mJob)


def update(
        db: Session, job_id: int, job_submit: sJob
        ) -> mJob:
    return update_item(db, job_submit, mJob, job_id)


def delete(db: Session, job_id: int, job: mJob) -> mJob:
    return update_item(db, sJob, job, job_id)
