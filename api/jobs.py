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
"""
    app.add_url_rule('/jobs', endpoint='jobs')
    app.add_url_rule('/jobs/create', endpoint='jobs.create')
    app.add_url_rule('/jobs/<int:id>/update', endpoint='jobs.update')
    app.add_url_rule('/jobs/<int:id>/delete', endpoint='jobs.delete')
"""