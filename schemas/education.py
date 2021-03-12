from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class Education(BaseModel):
    school: str
    degree: str
    start_date: Optional[datetime]
    end_date: Optional[datetime]
    status: str
