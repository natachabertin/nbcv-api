from typing import Optional

from pydantic import BaseModel


class SkillBase(BaseModel):
    name: str
    level: int
    category: str


class SkillCreate(SkillBase):
    pass


class SkillUpdate(SkillBase):
    name: Optional[str]
    level: Optional[int]
    category: Optional[str]


class Skill(SkillBase):
    id: int

    class Config:
        orm_mode = True
