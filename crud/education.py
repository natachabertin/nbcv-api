from typing import List

from sqlalchemy.orm import Session

from crud.base import select_item_by_id, list_items
from models.education import Education as mEducation
from schemas.education import Education as sEducation


def select_by_id(db: Session, ed_id: int) -> mEducation:
    return select_item_by_id(db, mEducation, ed_id)


def get_all(
        db: Session, skip: int = 0, limit: int = 100
        ) -> List[mEducation]:
    return list_items(db, mEducation, skip, limit)


def create(db: Session, education: sEducation) -> mEducation:
    db_ed = mEducation(
        school=education.school,
        degree=education.degree,
        status=education.status
    )
    db.add(db_ed)
    db.commit()
    db.refresh(db_ed)
    return db_ed


def update(db: Session, ed_id: int, education: mEducation) -> mEducation:
    return select_by_id(db, ed_id)
