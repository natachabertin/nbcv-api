from typing import List

import fastapi
from fastapi import Depends
from sqlalchemy.orm import Session

from crud import education as crud
from models.database import get_db
from schemas.education import Education


router = fastapi.APIRouter()


@router.get('/education', name='all_education')
def get_education(
        skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
        ) -> List[Education]:
    return crud.get_all(db, skip=skip, limit=limit)


@router.post('/education', name='add_education',
             status_code=201, response_model=Education)
def create_education(
        education: Education, db: Session = Depends(get_db)
        ) -> Education:
    return crud.create(db=db, education=education)


@router.get('/education/{ed_id}', name='get_education')
def get_education(
        ed_id: int, db: Session = Depends(get_db)
        ) -> Education:
    db_education = crud.select_by_id(db, ed_id=ed_id)
    return db_education


@router.put('/education/{ed_id}', name='update_education')
def update_education(
        ed_id: int, db: Session = Depends(get_db)
        ) -> Education:
    return Education


@router.delete('/education/{ed_id}', name='delete_education')
def delete_education(
        ed_id: int, db: Session = Depends(get_db)
        ) -> Education:
    return Education
