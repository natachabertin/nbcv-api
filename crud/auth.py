from fastapi import HTTPException, status
from fastapi.security import HTTPBasicCredentials
from sqlalchemy.orm import Session

from crud.users import get_user_by_username
from errors.security import WrongPasswordException
from utils.auth import verify_password


def validate_credentials(db: Session, credentials: HTTPBasicCredentials):
    user = get_user_by_username(db, credentials.username)
    if user is None:
        raise ValueError("That username is not registered.")
    if not verify_password(user.password, credentials.password):
        raise WrongPasswordException("Password incorrect.")

    return user


def get_current_user(db: Session, credentials: HTTPBasicCredentials):
    # TODO: Consider refactor this to crud.users
    try:
        return validate_credentials(db, credentials)
    except (ValueError, WrongPasswordException) as err:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=err.args[0],
            headers={"WWW-Authenticate": "Basic"},
        )