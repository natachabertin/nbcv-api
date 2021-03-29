from typing import List

import fastapi
from fastapi import Depends, Response
from security.jwt_auth import is_active_superuser
from sqlalchemy.orm import Session

from crud import projects as crud
from models.database import get_db
from schemas.projects import Project, ProjectCreate, ProjectUpdate


router = fastapi.APIRouter()


@router.get('/', name='all_projects', response_model=List[Project])
def get_projects(
        skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
        ) -> List[Project]:
    return crud.get_all(db, skip=skip, limit=limit)


@router.post('/', name='add_project', status_code=201, response_model=Project,
             dependencies=[Depends(is_active_superuser())])
def create_project(project: ProjectCreate, db: Session = Depends(get_db)) -> Project:

    return crud.create(db=db, project=project)


@router.get('/{project_id}', name='get_project', response_model=Project)
def get_project(project_id: int, db: Session = Depends(get_db)) -> Project:
    db_project = crud.select_by_id(db, project_id=project_id)
    return db_project


@router.patch('/{project_id}', name='update_project', response_model=Project,
             dependencies=[Depends(is_active_superuser())])
def update_project(project_id: int, project: ProjectUpdate, db: Session = Depends(get_db)) -> Project:
    return crud.update(db=db, project_id=project_id, project_submit=project)


@router.delete('/{project_id}', name='delete_project', status_code=204, response_class=Response,
             dependencies=[Depends(is_active_superuser())])
def delete_project(project_id: int, db: Session = Depends(get_db)):
    return crud.delete(db=db, project_id=project_id)
