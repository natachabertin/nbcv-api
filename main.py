import uvicorn
from fastapi import FastAPI

from api import (
    home, education, jobs, trainings, languages, skills, projects, users
)
from dependencies.database import engine, Base


Base.metadata.create_all(bind=engine)


api = FastAPI()


def configure_routing():
    api.include_router(home.router)
    api.include_router(
        users.router, prefix="/users", tags=['Users']
    )
    api.include_router(
        education.router, prefix="/education", tags=['Formal education']
    )
    api.include_router(
        jobs.router, prefix="/jobs", tags=['Job experience']
    )
    api.include_router(
        trainings.router, prefix="/trainings", tags=['Further trainings']
                       )
    api.include_router(
        skills.router, prefix="/skills", tags=['Skills']
    )
    api.include_router(
        projects.router, prefix="/projects", tags=['Portfolio']
                       )
    api.include_router(
        languages.router, prefix="/languages", tags=['Languages']
                       )


def configure():
    configure_routing()


if __name__ == '__main__':
    # test and debug
    configure()
    uvicorn.run(api, port=8000, host='127.0.0.1')
else:
    # prod
    configure()
