from pydantic import BaseModel


class Language(BaseModel):
    name: str
    written_level: int
    spoken_level: int
    level_description: str

    class Config:
        orm_mode = True
