from typing import List

import fastapi
from fastapi import Depends, Response
from sqlalchemy.orm import Session

from crud import jobs as crud
from models.database import get_db
from schemas.jobs import Job


router = fastapi.APIRouter()


@router.get('/', name='all_jobs')
def get_jobs(
        skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
        ) -> List[Job]:
    return crud.get_all(db, skip=skip, limit=limit)


@router.post('/', name='add_job', status_code=201, response_model=Job)
def create_job(job: Job, db: Session = Depends(get_db)) -> Job:

    return crud.create(db=db, job=job)


@router.get('/{job_id}', name='get_job')
def get_job(job_id: int, db: Session = Depends(get_db)) -> Job:
    db_job = crud.select_by_id(db, job_id=job_id)
    return db_job


@router.patch('/{job_id}', name='update_job')
def update_job(job_id: int, job: Job, db: Session = Depends(get_db)) -> Job:
    return crud.update(db=db, job_id=job_id, job_submit=job)


@router.delete('/{job_id}', name='delete_job', status_code=204, response_class=Response)
def delete_job(job_id: int, db: Session = Depends(get_db)):
    return crud.delete(db=db, job_id=job_id)
