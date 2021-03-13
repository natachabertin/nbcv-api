from typing import List

from sqlalchemy.orm import Session

from models.users import User as mUser
from schemas.users import User as sUser


def select_by_id(db: Session, user_id: int) -> mUser:
    return db.query(mUser).filter(mUser.id == user_id).first()


def get_all(db: Session, skip: int = 0, limit: int = 100) -> List[mUser]:
    return db.query(mUser).offset(skip).limit(limit).all()


def create(db: Session, user: sUser) -> mUser:
    db_user = mUser(
        username=user.username,
        email=user.email,
        password=user.password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update(db: Session, user_id: int, user: mUser) -> mUser:
    return select_by_id(db, user_id)
