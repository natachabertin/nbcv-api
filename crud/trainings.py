from typing import List

from sqlalchemy.orm import Session

from crud.base import select_item_by_id, list_items, create_item, update_item, \
    delete_item
from models.trainings import Training as mTraining
from schemas.trainings import Training as sTraining


def select_by_id(db: Session, training_id: int) -> mTraining:
    return select_item_by_id(db, mTraining, training_id)


def get_all(db: Session, skip: int = 0, limit: int = 100) -> List[mTraining]:
    return list_items(db, mTraining, skip, limit)


def create(db: Session, training: sTraining) -> mTraining:
    return create_item(db, training, mTraining)


def update(
        db: Session, training_id: int, training_submit: sTraining
        ) -> mTraining:
    return update_item(db, training_submit, mTraining, training_id)


def delete(db: Session, training_id: int):
    return delete_item(db, mTraining, training_id)