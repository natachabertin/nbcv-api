from typing import Any, Dict

from starlette.requests import Request

from schemas.users import UserDB

# TODO: implement proper logger.
# TODO: implement emails


def on_after_register(user: UserDB, request: Request):
    print(f"Email: User {user.id} has been registered.")


def on_after_forgot_password(user: UserDB, token: str, request: Request):
    print(f"Email: User {user.id} has forgot their password. Reset token: {token}")


def on_after_reset_password(user: UserDB, request: Request):
    print(f"Email: User {user.id} has reset their password.")


def on_after_update(user: UserDB, updated_user_data: Dict[str, Any], request: Request):
    print(f"LOG: User {user.id} has been updated with the following data: {updated_user_data}")


def after_verification_request(user: UserDB, token: str, request: Request):
    print(f"Email: Verification requested for user {user.id}. Verification token: {token}")


def after_verification(user: UserDB, request: Request):
    print(f"Email + LOG: {user.id} is now verified.")