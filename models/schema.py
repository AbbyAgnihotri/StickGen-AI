from pydantic import BaseModel
from typing import List

class Character(BaseModel):

    name:str

    shirt:str

    pants:str

    hair:str

class Scene(BaseModel):

    scene:int

    caption:str

    description:str



class Story(BaseModel):

    title:str

    characters:List[Character]

    scenes:List[Scene]