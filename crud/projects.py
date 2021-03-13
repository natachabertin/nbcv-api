from typing import List

from sqlalchemy.orm import Session

from models.projects import Project as mProject
from schemas.projects import Project as sProject


def select_by_id(db: Session, project_id: int) -> mProject:
    return db.query(mProject).filter(mProject.id == project_id).first()


def get_all(db: Session, skip: int = 0, limit: int = 100) -> List[mProject]:
    return db.query(mProject).offset(skip).limit(limit).all()


def create(db: Session, project: sProject) -> mProject:
    db_project = mProject(
        name=project.name,
        description=project.description,
        start_date=project.start_date,
        end_date=project.end_date
    )
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project


def update(db: Session, project_id: int, project: mProject) -> mProject:
    return select_by_id(db, project_id)
