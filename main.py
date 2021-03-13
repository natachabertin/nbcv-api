import uvicorn
from fastapi import FastAPI

from api import home, education, jobs, trainings, languages, skills, projects
from models.database import engine, Base

Base.metadata.create_all(bind=engine)

api = FastAPI()


def configure_routing():
    api.include_router(home.router)
    api.include_router(education.router, tags=['Formal education'])
    api.include_router(jobs.router, tags=['Job experience'])
    api.include_router(trainings.router, tags=['Further trainings'])
    api.include_router(skills.router, tags=['Skills'])
    api.include_router(projects.router, tags=['Portfolio'])
    api.include_router(languages.router, tags=['Languages'])


def configure():
    configure_routing()


if __name__ == '__main__':
    # test and debug
    configure()
    uvicorn.run(api, port=8000, host='127.0.0.1')
else:
    # prod
    configure()
