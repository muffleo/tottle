from typing import Optional

from pydantic import BaseModel

from ..objects import user


class Entity(BaseModel):
    type: str
    offset: int
    length: int
    url: Optional[str] = ""
    user: Optional["user.User"] = None
    language: Optional[str] = ""
