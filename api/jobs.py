from typing import List

import fastapi
from fastapi import Depends
from sqlalchemy.orm import Session

from crud import jobs as crud
from models.database import get_db
from schemas.jobs import Job


router = fastapi.APIRouter()


@router.get('/', name='all_jobs', response_model=List[Job])
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


@router.put('/{job_id}', name='update_job')
def update_job(job_id: int, db: Session = Depends(get_db)) -> Job:
    return Job


@router.delete('/{job_id}', name='delete_job')
def delete_job(job_id: int, db: Session = Depends(get_db)) -> Job:
    return Job
