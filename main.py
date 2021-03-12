import uvicorn
from fastapi import FastAPI

from api import home, education, jobs
from models.database import engine, Base

Base.metadata.create_all(bind=engine)

api = FastAPI()


def configure_routing():
    api.include_router(home.router)
    api.include_router(education.router)
    api.include_router(jobs.router)


def configure():
    configure_routing()


if __name__ == '__main__':
    # test and debug
    configure()
    uvicorn.run(api, port=8000, host='127.0.0.1')
else:
    # prod
    configure()
