from typing import List

from sqlalchemy.orm import Session

from crud.base import select_item_by_id, list_items, create_item
from models.languages import Language as mLanguage
from schemas.languages import Language as sLanguage


def select_by_id(db: Session, language_id: int) -> mLanguage:
    return select_item_by_id(db, mLanguage, language_id)


def get_all(db: Session, skip: int = 0, limit: int = 100) -> List[mLanguage]:
    return list_items(db, mLanguage, skip, limit)


def create(db: Session, language: sLanguage) -> mLanguage:
   return create_item(db, language, mLanguage)


def update(db: Session, language_id: int, language: mLanguage) -> mLanguage:
    return select_by_id(db, language_id)
