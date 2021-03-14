from typing import List

from pydantic.main import BaseModel as Schema
from sqlalchemy.orm import Session

from models.database import Base as Model


def select_item_by_id(db: Session, entity: Model, entity_id: int) -> Model:
    return db.query(entity).filter(entity.id == entity_id).first()


def list_items(
        db: Session, entity: Model, skip: int = 0, limit: int = 100
        ) -> List[Model]:
    return db.query(entity).offset(skip).limit(limit).all()


def create_item(db: Session, entity_schema: Schema, entity_model: Model) -> Model:
    db_entity = entity_model(**entity_schema.dict())
    db.add(db_entity)
    db.commit()
    db.refresh(db_entity)
    return db_entity


def update_item(
        db: Session, entity_schema: Schema, entity_model: Model, entity_id: int
        ) -> Model:
    updated_item = select_item_by_id(db, entity_model, entity_id)
    update_data = entity_schema.dict(exclude_unset=True)
    updated_item = entity_model(**update_data)
    db.flush()
    db.commit()
    return updated_item
