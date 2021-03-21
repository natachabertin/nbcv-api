from typing import List

import fastapi
from fastapi import Depends
from sqlalchemy.orm import Session

from crud import languages as crud
from models.database import get_db
from schemas.languages import Language


router = fastapi.APIRouter()


@router.get('/', name='all_languages', response_model=List[Language])
def get_languages(
        skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
        ) -> List[Language]:
    return crud.get_all(db, skip=skip, limit=limit)


@router.post('/', name='add_language', status_code=201, response_model=Language)
def create_language(language: Language, db: Session = Depends(get_db)) -> Language:

    return crud.create(db=db, language=language)


@router.get('/{language_id}', name='get_language')
def get_language(language_id: int, db: Session = Depends(get_db)) -> Language:
    db_language = crud.select_by_id(db, language_id=language_id)
    return db_language


@router.patch('/{language_id}', name='update_language')
def update_language(language_id: int, language: Language, db: Session = Depends(get_db)) -> Language:
    return crud.update(
        db=db, language_submit=language, language_id=language_id
    )


@router.delete('/{language_id}', name='delete_language')
def delete_language(language_id: int, db: Session = Depends(get_db)) -> Language:
    return crud.delete(db=db, ed_id=language_id)
