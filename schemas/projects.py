from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class Project(BaseModel):
    name: str
    description: str
    start_date: Optional[datetime]
    end_date: Optional[datetime]

    class Config:
        orm_mode = True
