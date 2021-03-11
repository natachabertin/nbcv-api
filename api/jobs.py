from typing import List

import fastapi

from models.jobs import Job

router = fastapi.APIRouter()


@router.get('/jobs', name='all_jobs')
def get_jobs() -> List[Job]:
    return ['jobs', 'list']


@router.post('/jobs', name='add_jobs')
def post_jobs(jobs_submit: Job) -> Job:

    return Job


@router.get('/jobs/id', name='get_job')
def get_job(id: int) -> Job:

    return Job


@router.put('/jobs/id', name='update_job')
def update_job(id: int) -> Job:

    return Job


@router.delete('/jobs/id', name='delete_job')
def delete_job(id: int) -> Job:

    return Job