from datetime import date
from typing import Optional

from pydantic import BaseModel


class TrainingBase(BaseModel):
    title: str
    school: str
    end_date: date
    certificate: Optional[str]


class TrainingCreate(TrainingBase):
    pass


class TrainingUpdate(TrainingBase):
    title: Optional[str]
    school: Optional[str]
    end_date: Optional[date]
    certificate: Optional[str]


class Training(TrainingBase):
    id: int

    class Config:
        orm_mode = True
