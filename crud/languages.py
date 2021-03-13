from typing import List

from sqlalchemy.orm import Session

from models.languages import Language as mLanguage
from schemas.languages import Language as sLanguage


def select_by_id(db: Session, language_id: int) -> mLanguage:
    return db.query(mLanguage).filter(mLanguage.id == language_id).first()


def get_all(db: Session, skip: int = 0, limit: int = 100) -> List[mLanguage]:
    return db.query(mLanguage).offset(skip).limit(limit).all()


def create(db: Session, language: sLanguage) -> mLanguage:
    db_language = mLanguage(
        name=language.name,
        written_level=language.written_level,
        spoken_level=language.spoken_level,
        level_description=language.level_description
    )
    db.add(db_language)
    db.commit()
    db.refresh(db_language)
    return db_language


def update(db: Session, language_id: int, language: mLanguage) -> mLanguage:
    return select_by_id(db, language_id)
