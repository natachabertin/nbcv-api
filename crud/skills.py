from typing import List

from sqlalchemy.orm import Session

from models.skills import Skill as mSkill
from schemas.skills import Skill as sSkill


def select_by_id(db: Session, skill_id: int) -> mSkill:
    return db.query(mSkill).filter(mSkill.id == skill_id).first()


def get_all(db: Session, skip: int = 0, limit: int = 100) -> List[mSkill]:
    return db.query(mSkill).offset(skip).limit(limit).all()


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
