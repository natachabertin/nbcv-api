import fastapi
from fastapi import Depends, Response
from fastapi_users import fastapi_users

from security.jwt_auth import jwt_authentication

router = fastapi.APIRouter()


@router.post("/auth/jwt/refresh")
async def refresh_jwt(response: Response, user=Depends(fastapi_users.get_current_active_user)):
    return await jwt_authentication.get_login_response(user, response)