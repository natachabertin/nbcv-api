from sqlalchemy import Column, Integer, String

from models.database import Base


class Language(Base):
    __tablename__ = "languages"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    written_level = Column(Integer)
    spoken_level = Column(Integer)
    level_description = Column(String)
