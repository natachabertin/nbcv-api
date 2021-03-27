from sqlalchemy import Column, Integer, String, Date

from dependencies.database import Base


class Education(Base):
    __tablename__ = "education"

    id = Column(Integer, primary_key=True, index=True)
    school = Column(String)
    degree = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)
    status = Column(String)
