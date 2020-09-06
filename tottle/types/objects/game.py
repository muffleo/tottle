from pydantic import BaseModel
from typing import Optional, List

from tottle.types.objects.animation import Animation
from tottle.types.objects.message import MessageEntity
from tottle.types.objects.photo import PhotoSize


class CallbackGame(BaseModel):
    ...


class Game(BaseModel):
    title: str
    description: str
    photo: List[PhotoSize]
    text: Optional[str] = ""
    text_entities: Optional[List[MessageEntity]] = []
    animation: Optional[Animation] = None
