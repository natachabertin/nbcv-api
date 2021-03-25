from typing import List

from sqlalchemy.orm import Session

from crud.base import (
    select_item_by_id, list_items, create_item, update_item, delete_item
)
from models.education import Education as mEducation
from schemas.education import Education, EducationCreate, EducationUpdate


def select_by_id(db: Session, ed_id: int) -> mEducation:
    return select_item_by_id(db, mEducation, ed_id)


def get_all(
        db: Session, skip: int = 0, limit: int = 100
        ) -> List[Education]:
    return list_items(db, mEducation, skip, limit)


def create(db: Session, education: EducationCreate) -> mEducation:
    return create_item(db, education, mEducation)


def update(
        db: Session, ed_id: int, education_submit: EducationUpdate
        ) -> mEducation:
    return update_item(db, education_submit, mEducation, ed_id)


def delete(db: Session, ed_id: int):
    return delete_item(db, mEducation, ed_id)
