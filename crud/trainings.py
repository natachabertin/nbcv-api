from typing import List

from sqlalchemy.orm import Session

from crud.base import select_item_by_id, list_items
from models.trainings import Training as mTraining
from schemas.trainings import Training as sTraining


def select_by_id(db: Session, training_id: int) -> mTraining:
    return select_item_by_id(db, mTraining, training_id)


def get_all(db: Session, skip: int = 0, limit: int = 100) -> List[mTraining]:
    return list_items(db, mTraining, skip, limit)


def create(db: Session, training: sTraining) -> mTraining:
    db_training = mTraining(
        title=training.title,
        school=training.school,
        end_date=training.end_date,
        certificate=training.certificate,
    )
    db.add(db_training)
    db.commit()
    db.refresh(db_training)
    return db_training


def update(db: Session, training_id: int, training: mTraining) -> mTraining:
    return select_by_id(db, training_id)
