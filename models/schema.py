from typing import List
from pydantic import BaseModel, Field


class Character(BaseModel):
    """Represents a character appearing in the comic."""

    name: str
    gender: str
    shirt: str
    pants: str
    hair: str
    emotion: str = "Happy"


class Scene(BaseModel):
    """Represents one comic panel."""

    scene: int = Field(..., ge=1)
    caption: str
    description: str


class Story(BaseModel):
    """Complete storyboard."""

    title: str
    characters: List[Character]
    scenes: List[Scene]