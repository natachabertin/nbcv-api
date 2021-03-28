from starlette.requests import Request

from schemas.users import UserDB


def on_after_register(user: UserDB, request: Request):
    print(f"User {user.id} has registered.")
