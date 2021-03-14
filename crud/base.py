from sqlalchemy.orm import Session

from models.database import Base as Model


def select_item_by_id(db: Session, entity: Model, entity_id: int) -> Model:
    return db.query(entity).filter(entity.id == entity_id).first()
