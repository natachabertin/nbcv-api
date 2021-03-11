from models.education import Education

async def get_all():
    return ['education', 'list']

async def create(education: Education) -> Education:

    return await education

async def update(id: int, education: Education) -> Education:
    return await select_by_id(id)


async def select_by_id(id: int) -> Education:
    selected_education = id
    return await selected_education
