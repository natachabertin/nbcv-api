from typing import List

from sqlalchemy.orm import Session

from crud.base import select_item_by_id, list_items, create_item
from models.projects import Project as mProject
from schemas.projects import Project as sProject


def select_by_id(db: Session, project_id: int) -> mProject:
    return select_item_by_id(db, mProject, project_id)


def get_all(db: Session, skip: int = 0, limit: int = 100) -> List[mProject]:
    return list_items(db, mProject, skip, limit)


def create(db: Session, project: sProject) -> mProject:
    return create_item(db, project, mProject)


def update(db: Session, project_id: int, project: mProject) -> mProject:
    return select_by_id(db, project_id)
