from unittest.mock import Mock
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from crud.users import create
from dependencies.auth import security
from dependencies.database import Base, get_db
from main import api
from schemas.users import UserCreate

USER_DATA = UserCreate(
    username='admin', email='admin@mockmail.com', password='admin-Pwd123'
)

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)

Base.metadata.create_all(bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


def override_security(credentials: UserCreate):
    mock_security = Mock()
    mock_security.username.return_value = credentials.username
    mock_security.password.return_value = credentials.password

    return mock_security


def insert_user(user: UserCreate, db: Session):
    create(db=db, user=user)


def replace_db():
    api.dependency_overrides[get_db] = override_get_db


def replace_credentials(credentials: UserCreate):
    api.dependency_overrides[security] = override_security(credentials)


def get_client(credentials: UserCreate):
    replace_db()
    replace_credentials(credentials)
    client = TestClient(api)
    client.post("/users/", json={
        "username": credentials.username,
        "email": credentials.email,
        "password": credentials.password
    })

    return client


client = get_client(USER_DATA)
