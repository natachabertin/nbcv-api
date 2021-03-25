from typing import List

from sqlalchemy.orm import Session

from crud.base import (
    select_item_by_id, list_items, create_item, update_item, delete_item
)
from models.users import User as mUser
from schemas.users import User as User, UserCreate, UserUpdate, UserPwdUpdate


def select_by_id(db: Session, user_id: int) -> mUser:
    return select_item_by_id(db, mUser, user_id)


def get_all(db: Session, skip: int = 0, limit: int = 100) -> List[User]:
    return list_items(db, mUser, skip, limit)


def create(db: Session, user: UserCreate) -> mUser:
    return create_item(db, user, mUser)


def update(
        db: Session, user_id: int, user_submit: UserUpdate
        ) -> mUser:
    return update_item(db, user_submit, mUser, user_id)


def change_password(
        db: Session, user_id: int, user_submit: UserPwdUpdate
        ) -> mUser:
    return update_item(db, user_submit, mUser, user_id)


def delete(db: Session, user_id: int):
    return delete_item(db, mUser, user_id)
