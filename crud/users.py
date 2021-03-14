from typing import List

from sqlalchemy.orm import Session

from crud.base import select_item_by_id, list_items, create_item
from models.users import User as mUser
from schemas.users import User as sUser


def select_by_id(db: Session, user_id: int) -> mUser:
    return select_item_by_id(db, mUser, user_id)


def get_all(db: Session, skip: int = 0, limit: int = 100) -> List[mUser]:
    return list_items(db, mUser, skip, limit)


def create(db: Session, user: sUser) -> mUser:
    return create_item(db, user, mUser)


def update(db: Session, user_id: int, user: mUser) -> mUser:
    return select_by_id(db, user_id)
