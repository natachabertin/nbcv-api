from typing import List

import fastapi
from fastapi import Depends
from sqlalchemy.orm import Session

from crud import skills as crud
from models.database import get_db
from schemas.skills import Skill


router = fastapi.APIRouter()


@router.get('/', name='all_skills', response_model=List[Skill])
def get_skills(
        skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
        ) -> List[Skill]:
    return crud.get_all(db, skip=skip, limit=limit)


@router.post('/', name='add_skill', status_code=201, response_model=Skill)
def create_skill(skill: Skill, db: Session = Depends(get_db)) -> Skill:

    return crud.create(db=db, skill=skill)


@router.get('/{skill_id}', name='get_skill')
def get_skill(skill_id: int, db: Session = Depends(get_db)) -> Skill:
    db_skill = crud.select_by_id(db, skill_id=skill_id)
    return db_skill


@router.put('/{skill_id}', name='update_skill')
def update_skill(skill_id: int, db: Session = Depends(get_db)) -> Skill:
    return Skill


@router.delete('/{skill_id}', name='delete_skill')
def delete_skill(skill_id: int, db: Session = Depends(get_db)) -> Skill:
    return Skill