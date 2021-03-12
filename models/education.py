from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime

from database import Base


class Education(Base):
    __tablename__ = "education"

    id = Column(Integer, primary_key=True, index=True)
    school = Column(String)
    degree = Column(String)
    start_date = Column(DateTime, default=datetime.utcnow)
    end_date = Column(DateTime, default=datetime.utcnow)
    status = Column(String)
