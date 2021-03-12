from typing import List

import fastapi

from schemas.jobs import Job
from operations import jobs

router = fastapi.APIRouter()


@router.get('/jobs', name='all_jobs', response_model=List[Job])
async def get_jobs() -> List[Job]:
    return await jobs.get_all()


@router.post('/jobs', name='add_job', status_code=201, response_model=Job)
async def create_job(job: Job) -> Job:

    return await jobs.create(job)


@router.get('/jobs/{job_id}', name='get_job')
async def get_job(job_id: int) -> Job:

    return Job


@router.put('/jobs/{job_id}', name='update_job')
async def update_job(job_id: int) -> Job:

    return Job


@router.delete('/jobs/{job_id}', name='delete_job')
async def delete_job(job_id: int) -> Job:

    return Job
