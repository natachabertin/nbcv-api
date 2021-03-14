from typing import List

from sqlalchemy.orm import Session

from crud.base import select_item_by_id, list_items
from models.skills import Skill as mSkill
from schemas.skills import Skill as sSkill


def select_by_id(db: Session, skill_id: int) -> mSkill:
    return select_item_by_id(db, mSkill, skill_id)


def get_all(db: Session, skip: int = 0, limit: int = 100) -> List[mSkill]:
    return list_items(db, mSkill, skip, limit)


def create(db: Session, skill: sSkill) -> mSkill:
    db_skill = mSkill(
        name=skill.name,
        level=skill.level,
        category=skill.category
    )
    db.add(db_skill)
    db.commit()
    db.refresh(db_skill)
    return db_skill


def update(db: Session, skill_id: int, skill: mSkill) -> mSkill:
    return select_by_id(db, skill_id)
