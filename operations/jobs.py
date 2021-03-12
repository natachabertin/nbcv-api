from schemas.jobs import Job


async def get_all():
    return ['jobs', 'list']


async def create(job: Job) -> Job:
    return await {**job.dict()}


async def update(job_id: int, job: Job) -> Job:
    return await select_by_id(job_id)


async def select_by_id(job_id: int) -> Job:
    selected_job = job_id
    return await selected_job
