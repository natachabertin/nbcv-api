from typing import List

from sqlalchemy.orm import Session

from models.database import Base as Model


def select_item_by_id(db: Session, entity: Model, entity_id: int) -> Model:
    return db.query(entity).filter(entity.id == entity_id).first()


def list_items(
        db: Session, entity: Model, skip: int = 0, limit: int = 100
        ) -> List[Model]:
    return db.query(entity).offset(skip).limit(limit).all()