from typing import List

import fastapi

from models.education import Education

router = fastapi.APIRouter()


@router.get('/education', name='all_education')
def get_education() -> List[Education]:
    return ['education', 'list']


@router.post('/education', name='add_education')
def post_education(education_submit: Education) -> Education:

    return Education


@router.get('/education/id', name='get_education')
def get_education(id: int) -> Education:

    return Education


@router.put('/education/id', name='update_education')
def update_education(id: int) -> Education:

    return Education


@router.delete('/education/id', name='delete_education')
def delete_education(id: int) -> Education:

    return Education
