from typing import Optional

from pydantic import BaseModel


class LanguageBase(BaseModel):
    name: str
    written_level: int
    spoken_level: int
    level_description: str


class LanguageCreate(LanguageBase):
    pass

class LanguageUpdate(LanguageBase):
    name: Optional[str]
    written_level: Optional[int]
    spoken_level: Optional[int]
    level_description: Optional[str]


class Language(LanguageBase):
    id: int

    class Config:
        orm_mode = True
