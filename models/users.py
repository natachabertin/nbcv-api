from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase

from models.database import Base, SessionLocal
from schemas.users import UserDB


class UserTable(Base, SQLAlchemyBaseUserTable):
    pass


users = UserTable.__table__

user_db = SQLAlchemyUserDatabase(UserDB, SessionLocal, users)
