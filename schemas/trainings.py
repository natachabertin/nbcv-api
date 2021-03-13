from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class Training(BaseModel):
    title: str
    school: str
    end_date: datetime
    certificate: Optional[str]

    class Config:
        orm_mode = True
