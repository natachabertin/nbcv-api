from typing import List

from sqlalchemy.orm import Session

from models.education import Education as mEducation
from schemas.education import Education as sEducation


async def select_by_id(db: Session, ed_id: int) -> mEducation:
    return await db.query(mEducation).filter(mEducation.id == ed_id).first()


async def get_all(
        db: Session, skip: int = 0, limit: int = 100
        ) -> List[mEducation]:
    return db.query(mEducation).offset(skip).limit(limit).all()


async def create(db: Session, education: sEducation) -> mEducation:
    db_ed = mEducation(
        school=education.school,
        degree=education.degree,
        status=education.status
    )
    db.add(db_ed)
    db.commit()
    db.refresh(db_ed)
    return await db_ed


async def update(db: Session, ed_id: int, education: mEducation) -> mEducation:
    return await select_by_id(db, ed_id)
