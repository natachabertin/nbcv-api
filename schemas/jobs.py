from datetime import date
from typing import Optional

from pydantic import BaseModel


class JobBase(BaseModel):
    title: str
    company: str
    start_date: date
    end_date: date
    achievements: str


class JobCreate(JobBase):
    pass


class JobUpdate(BaseModel):
    title: Optional[str]
    company: Optional[str]
    start_date: Optional[date]
    end_date: Optional[date]
    achievements: Optional[str]


class Job(JobBase):
    id: int

    class Config:
        orm_mode = True
