from typing import List

import fastapi
from fastapi import Depends
from sqlalchemy.orm import Session

from crud import languages as crud
from models.database import get_db
from schemas.languages import Language


router = fastapi.APIRouter()


@router.get('/languages', name='all_languages', response_model=List[Language])
def get_languages(
        skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
        ) -> List[Language]:
    return crud.get_all(db, skip=skip, limit=limit)


@router.post('/languages', name='add_language', status_code=201, response_model=Language)
def create_language(language: Language, db: Session = Depends(get_db)) -> Language:

    return crud.create(db=db, language=language)


@router.get('/languages/{language_id}', name='get_language')
def get_language(language_id: int, db: Session = Depends(get_db)) -> Language:
    db_language = crud.select_by_id(db, language_id=language_id)
    return db_language


@router.put('/languages/{language_id}', name='update_language')
def update_language(language_id: int, db: Session = Depends(get_db)) -> Language:
    return Language


@router.delete('/languages/{language_id}', name='delete_language')
def delete_language(language_id: int, db: Session = Depends(get_db)) -> Language:
    return Language
