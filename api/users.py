from typing import List

import fastapi
from fastapi import Depends
from sqlalchemy.orm import Session

from crud import users as crud
from models.database import get_db
from schemas.users import User


router = fastapi.APIRouter()


@router.get('/', name='all_users', response_model=List[User])
def get_users(
        skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
        ) -> List[User]:
    return crud.get_all(db, skip=skip, limit=limit)


@router.post('/', name='add_user', status_code=201, response_model=User)
def create_user(user: User, db: Session = Depends(get_db)) -> User:

    return crud.create(db=db, user=user)


@router.get('/{user_id}', name='get_user')
def get_user(user_id: int, db: Session = Depends(get_db)) -> User:
    db_user = crud.select_by_id(db, user_id=user_id)
    return db_user


@router.put('/{user_id}', name='update_user')
def update_user(user_id: int, db: Session = Depends(get_db)) -> User:
    return User


@router.delete('/{user_id}', name='delete_user')
def delete_user(user_id: int, db: Session = Depends(get_db)) -> User:
    return User
