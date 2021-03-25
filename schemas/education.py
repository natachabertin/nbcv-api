from datetime import date
from typing import Optional

from pydantic import BaseModel


class EducationBase(BaseModel):
    school: str
    degree: str
    start_date: date
    end_date: date
    status: str


class EducationCreate(EducationBase):
    pass


class EducationUpdate(BaseModel):
    school: Optional[str]
    degree: Optional[str]
    start_date: Optional[date]
    end_date: Optional[date]
    status: Optional[str]


class Education(EducationBase):
    id: int

    class Config:
        orm_mode = True
