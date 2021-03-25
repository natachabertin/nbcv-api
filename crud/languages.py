from typing import List

from sqlalchemy.orm import Session

from crud.base import (
    select_item_by_id, list_items, create_item, update_item, delete_item
)
from models.languages import Language as mLanguage
from schemas.languages import Language, LanguageCreate, LanguageUpdate


def select_by_id(db: Session, language_id: int) -> mLanguage:
    return select_item_by_id(db, mLanguage, language_id)


def get_all(db: Session, skip: int = 0, limit: int = 100) -> List[Language]:
    return list_items(db, mLanguage, skip, limit)


def create(db: Session, language: LanguageCreate) -> mLanguage:
    return create_item(db, language, mLanguage)


def update(db: Session, language_id: int, language_submit: LanguageUpdate) -> mLanguage:
    return update_item(db, language_submit, mLanguage, language_id)


def delete(db: Session, language_id: int):
    return delete_item(db, mLanguage, language_id)
