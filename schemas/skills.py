from pydantic import BaseModel


class Skill(BaseModel):
    name: str
    level: str
    category: str

    class Config:
        orm_mode = True
