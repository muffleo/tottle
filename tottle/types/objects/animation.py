from typing import Optional

from pydantic import BaseModel

from ..objects import photo


class Animation(BaseModel):
    file_id: str
    file_unique_id: str
    width: int
    height: int
    duration: int
    thumb: Optional["photo.PhotoSize"] = None
    file_name: Optional[str] = ""
    mime_type: Optional[str] = ""
    file_size: Optional[int] = 0
