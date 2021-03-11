from models.jobs import Job

async def get_all():

    return ['jobs', 'list']

async def create(job: Job) -> Job:

    return await job


async def update(id: int, job: Job) -> Job:

    return await select_by_id(id)


async def select_by_id(id: int) -> Job:
    selected_job = id

    return await selected_job
