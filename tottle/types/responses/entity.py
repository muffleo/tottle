from typing import Optional

from pydantic import BaseModel

from tottle.types.responses.user import User


class Entity(BaseModel):
    type: str
    offset: int
    length: int
    url: Optional[str] = None
    user: Optional["User"] = None
    language: Optional[str] = None
