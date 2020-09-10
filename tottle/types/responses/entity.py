from typing import Optional

from pydantic import BaseModel

from ..responses.user import User


class Entity(BaseModel):
    type: str
    offset: int
    length: int
    url: Optional[str] = ""
    user: Optional["User"] = None
    language: Optional[str] = ""
