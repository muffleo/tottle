from typing import Optional

from pydantic import BaseModel

from ..responses.photo import PhotoSize


class Audio(BaseModel):
    file_id: str
    file_unique_id: str
    duration: int
    performer: Optional[str] = ""
    title: Optional[str] = ""
    mime_type: Optional[str] = ""
    file_size: Optional[int] = 0
    thumb: Optional["PhotoSize"] = None
