from typing import List

from sqlalchemy.orm import Session

from crud.base import (
    select_item_by_id, list_items, create_item, update_item, delete_item
)
from models.skills import Skill as mSkill
from schemas.skills import Skill, SkillCreate, SkillUpdate


def select_by_id(db: Session, skill_id: int) -> mSkill:
    return select_item_by_id(db, mSkill, skill_id)


def get_all(db: Session, skip: int = 0, limit: int = 100) -> List[Skill]:
    return list_items(db, mSkill, skip, limit)


def create(db: Session, skill: SkillCreate) -> mSkill:
    return create_item(db, skill, mSkill)


def update(
        db: Session, skill_id: int, skill_submit: SkillUpdate
        ) -> mSkill:
    return update_item(db, skill_submit, mSkill, skill_id)


def delete(db: Session, skill_id: int):
    return delete_item(db, mSkill, skill_id)
