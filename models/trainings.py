from sqlalchemy import Column, Integer, String, Date

from models.database import Base


class Training(Base):
    __tablename__ = "trainings"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    school = Column(String)
    end_date = Column(Date)
    certificate = Column(String)
