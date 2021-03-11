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
"""
    app.add_url_rule('/education', endpoint='education')
    app.add_url_rule('/education/create', endpoint='education.create')
    app.add_url_rule('/education/<int:id>/update', endpoint='education.update')
    app.add_url_rule('/education/<int:id>/delete', endpoint='education.delete')
"""