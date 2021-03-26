import secrets
from typing import List

import fastapi
from fastapi import Depends, Response, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from sqlalchemy.orm import Session

from crud import users as crud
from dependencies.database import get_db
from schemas.users import User, UserCreate, UserUpdate, UserPwdUpdate


router = fastapi.APIRouter()


security = HTTPBasic()


def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, "stanleyjobson")
    correct_password = secrets.compare_digest(credentials.password, "swordfish")
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username


@router.get('/', name='all_users', response_model=List[User])
def get_users(
        skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
        ) -> List[User]:
    return crud.get_all(db, skip=skip, limit=limit)


@router.get("/me")
def read_current_user(username: str = Depends(get_current_username)):
    return {"username": username}


@router.post('/', name='add_user', status_code=201, response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)) -> User:
    return crud.create(db=db, user=user)


@router.get('/{user_id}', name='get_user', response_model=User)
def get_user(user_id: int, db: Session = Depends(get_db)) -> User:
    db_user = crud.select_by_id(db, user_id=user_id)
    return db_user


@router.patch('/{user_id}', name='update_user', response_model=User)
def update_user(
        user_id: int, user: UserUpdate, db: Session = Depends(get_db)
        ) -> User:
    return crud.update(db=db, user_id=user_id, user_submit=user)


@router.patch(
    '/{user_id}/change_password', name='change_password', response_model=User
)
def update_user_pwd(
        user_id: int, user: UserPwdUpdate, db: Session = Depends(get_db)
        ) -> User:
    return crud.change_password(db=db, user_id=user_id, user_submit=user)


@router.delete(
    '/{user_id}',
    name='delete_user',
    status_code=204,
    response_class=Response
)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return crud.delete(db=db, user_id=user_id)
