from typing import Optional, List

from pydantic import BaseModel

from ..responses.animation import Animation
from ..responses.entity import Entity
from ..responses.photo import PhotoSize


class CallbackGame(BaseModel):
    ...


class Game(BaseModel):
    title: str
    description: str
    photo: List[PhotoSize]
    text: Optional[str] = ""
    text_entities: Optional[List[Entity]] = []
    animation: Optional[Animation] = None
