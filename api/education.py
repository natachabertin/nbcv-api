from typing import List

import fastapi

from schemas.education import Education

router = fastapi.APIRouter()


@router.get('/education', name='all_education')
async def get_education() -> List[Education]:
    return ['education', 'list']


@router.post('/education', name='add_education', status_code=201, response_model=Education)
async def create_education(education: Education) -> Education:
    education_dict = education.dict()

    return education_dict


@router.get('/education/{ed_id}', name='get_education')
async def get_education(ed_id: int) -> Education:

    return Education


@router.put('/education/{ed_id}', name='update_education')
async def update_education(ed_id: int) -> Education:

    return Education


@router.delete('/education/{ed_id}', name='delete_education')
async def delete_education(ed_id: int) -> Education:

    return Education
