from typing import List

import fastapi

from models.jobs import Job
from operations import jobs

router = fastapi.APIRouter()


@router.get('/jobs', name='all_jobs', response_model=List[Job])
async def get_jobs() -> List[Job]:
    return await jobs.get_all()


@router.post('/jobs', name='add_job', status_code=201, response_model=Job)
async def create_job(job: Job) -> Job:

    return await jobs.create(**job)


@router.get('/jobs/{id}', name='get_job')
async def get_job(id: int) -> Job:

    return Job


@router.put('/jobs/{id}', name='update_job')
async def update_job(id: int) -> Job:

    return Job


@router.delete('/jobs/{id}', name='delete_job')
async def delete_job(id: int) -> Job:

    return Job
