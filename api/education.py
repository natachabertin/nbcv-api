from typing import List

import fastapi
from fastapi import Depends, Response
from sqlalchemy.orm import Session

from crud import education as crud
from dependencies.database import get_db
from schemas.education import Education, EducationCreate, EducationUpdate


router = fastapi.APIRouter()


@router.get('/', name='all_education', response_model=List[Education])
def get_educations(
        skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
        ) -> List[Education]:
    return crud.get_all(db, skip=skip, limit=limit)


@router.post('/', name='add_education',
             status_code=201, response_model=Education)
def create_education(
        education: EducationCreate, db: Session = Depends(get_db)
        ) -> Education:
    return crud.create(db=db, education=education)


@router.get('/{ed_id}', name='get_education', response_model=Education)
def get_education(
        ed_id: int, db: Session = Depends(get_db)
        ) -> Education:
    db_education = crud.select_by_id(db, ed_id=ed_id)
    return db_education


@router.patch('/{ed_id}', name='update_education', response_model=Education)
def update_education(
        ed_id: int, education: EducationUpdate, db: Session = Depends(get_db)
        ) -> Education:
    return crud.update(db=db, ed_id=ed_id, education_submit=education)


@router.delete(
    '/{ed_id}',
    name='delete_education',
    status_code=204,
    response_class=Response
)
def delete_education(ed_id: int, db: Session = Depends(get_db)):
    return crud.delete(db=db, ed_id=ed_id)
