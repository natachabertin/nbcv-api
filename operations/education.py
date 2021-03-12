from schemas.education import Education


async def get_all():
    return ['education', 'list']


async def create(education: Education) -> Education:
    return await education


async def update(ed_id: int, education: Education) -> Education:
    return await select_by_id(ed_id)


async def select_by_id(ed_id: int) -> Education:
    selected_education = ed_id
    return await selected_education
