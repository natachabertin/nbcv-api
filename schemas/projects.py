from datetime import date
from typing import Optional

from pydantic import BaseModel


class ProjectBase(BaseModel):
    name: str
    description: str
    start_date: date
    end_date: date


class ProjectCreate(ProjectBase):
    pass


class ProjectUpdate(ProjectBase):
    name: Optional[str]
    description: Optional[str]
    start_date: Optional[date]
    end_date: Optional[date]


class Project(ProjectBase):
    id: int

    class Config:
        orm_mode = True
