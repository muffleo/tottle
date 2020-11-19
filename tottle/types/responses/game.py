from typing import Optional, List

from pydantic import BaseModel

from tottle.types.responses.animation import Animation
from tottle.types.responses.entity import Entity
from tottle.types.responses.photo import PhotoSize


class CallbackGame(BaseModel):
    ...


class Game(BaseModel):
    title: str
    description: str
    photo: List[PhotoSize]
    text: Optional[str] = None
    text_entities: Optional[List[Entity]] = None
    animation: Optional[Animation] = None
