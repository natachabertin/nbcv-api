from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime

from models.database import Base


class Training(Base):
    __tablename__ = "trainings"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    school = Column(String)
    end_date = Column(DateTime, default=datetime.utcnow)
    certificate = Column(String)
