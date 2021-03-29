from sqlalchemy import Column, Integer, String

from models.database import Base


class Skill(Base):
    __tablename__ = "skills"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    level = Column(Integer)
    category = Column(String)
