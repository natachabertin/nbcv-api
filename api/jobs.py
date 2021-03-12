from typing import List

import fastapi
from fastapi import Depends
from sqlalchemy.orm import Session

from crud import jobs as crud
from models.database import get_db
from schemas.jobs import Job


router = fastapi.APIRouter()


@router.get('/jobs', name='all_jobs', response_model=List[Job])
async def get_jobs(
        skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
        ) -> List[Job]:
    return await crud.get_all(db, skip=skip, limit=limit)


@router.post('/jobs', name='add_job', status_code=201, response_model=Job)
async def create_job(job: Job, db: Session = Depends(get_db)) -> Job:

    return await crud.create(db=db, job=job)


@router.get('/jobs/{job_id}', name='get_job')
async def get_job(job_id: int, db: Session = Depends(get_db)) -> Job:
    db_job = await crud.select_by_id(db, job_id=job_id)
    return db_job


@router.put('/jobs/{job_id}', name='update_job')
async def update_job(job_id: int, db: Session = Depends(get_db)) -> Job:
    return Job


@router.delete('/jobs/{job_id}', name='delete_job')
async def delete_job(job_id: int, db: Session = Depends(get_db)) -> Job:
    return Job
