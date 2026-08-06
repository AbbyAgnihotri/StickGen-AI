from pydantic import BaseModel
from typing import List

class Character(BaseModel):

    name:str

    gender:str

    shirt:str

    pants:str

    hair:str

    emotion: str = "happy"

    age: int | None = None


class Scene(BaseModel):

    scene:int

    caption:str

    description:str



class Story(BaseModel):

    title:str

    characters:List[Character]

    scenes:List[Scene]