from datetime import datetime

from sqlalchemy import Boolean, Column, Integer, String, DateTime

from .database import Base


class Jobs(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    company = Column(String)
    start_date = Column(DateTime, default=datetime.datetime.utcnow)
    end_date = Column(DateTime, default=datetime.datetime.utcnow)
    achievements = Column(String)
