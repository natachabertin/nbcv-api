from typing import Optional

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    pass


class UserCreate(UserBase):
    password: str
    username: str
    email: EmailStr


class UserUpdate(UserBase):
    username: Optional[str]
    email: Optional[EmailStr]


class UserPwdUpdate(UserBase):
    password: str


class User(UserBase):
    id: int
    username: str
    email: EmailStr

    class Config:
        orm_mode = True
