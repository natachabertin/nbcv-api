from typing import List

from fastapi_users import FastAPIUsers
from fastapi_users.authentication import JWTAuthentication

from models.users import user_db
from schemas.users import User, UserCreate, UserUpdate, UserDB

# TODO: After MVP, refact to read from a gitignored file.
SECRET = "SECRET"

auth_backends: List = []

jwt_authentication = JWTAuthentication(
    secret=SECRET,
    lifetime_seconds=3600,
    name="nbcv-jwt",
)

auth_backends.append(jwt_authentication)

fastapi_users = FastAPIUsers(
    user_db,
    auth_backends,
    User,
    UserCreate,
    UserUpdate,
    UserDB,
)

def is_active_superuser():
    return fastapi_users.current_user(active=True, superuser=True)