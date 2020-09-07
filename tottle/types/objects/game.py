from typing import Optional, List

from pydantic import BaseModel

from ..objects import animation, entity, photo


class CallbackGame(BaseModel):
    ...


class Game(BaseModel):
    title: str
    description: str
    photo: List["photo.PhotoSize"]
    text: Optional[str] = ""
    text_entities: Optional[List["entity.Entity"]] = []
    animation: Optional["animation.Animation"] = None
