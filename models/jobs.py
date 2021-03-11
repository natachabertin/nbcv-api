from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class Job(BaseModel):
    title: str
    company: str
    start_date: Optional[datetime]
    end_date: Optional[datetime]
    achievements: str
