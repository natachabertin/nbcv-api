from typing import List

import fastapi
from fastapi import Depends, Response
from sqlalchemy.orm import Session

from crud import languages as crud
from models.database import get_db
from schemas.languages import Language, LanguageCreate, LanguageUpdate


router = fastapi.APIRouter()


@router.get('/', name='all_languages', response_model=List[Language])
def get_languages(
        skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
        ) -> List[Language]:
    return crud.get_all(db, skip=skip, limit=limit)


@router.post('/', name='add_language', status_code=201, response_model=Language)
def create_language(language: LanguageCreate, db: Session = Depends(get_db)) -> Language:
    return crud.create(db=db, language=language)


@router.get('/{language_id}', name='get_language', response_model=Language)
def get_language(language_id: int, db: Session = Depends(get_db)) -> Language:
    db_language = crud.select_by_id(db, language_id=language_id)
    return db_language


@router.patch('/{language_id}', name='update_language', response_model=Language)
def update_language(
        language_id: int, language: LanguageUpdate, db: Session = Depends(get_db)
        ) -> Language:
    return crud.update(
        db=db, language_id=language_id, language_submit=language
    )


@router.delete('/{language_id}', name='delete_language', status_code=204, response_class=Response)
def delete_language(language_id: int, db: Session = Depends(get_db)):
    return crud.delete(db=db, language_id=language_id)
