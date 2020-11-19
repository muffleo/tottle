from typing import Optional

from pydantic import BaseModel

from tottle.types.responses.photo import PhotoSize


class Audio(BaseModel):
    file_id: str
    file_unique_id: str
    duration: int
    performer: Optional[str] = None
    title: Optional[str] = None
    mime_type: Optional[str] = None
    file_size: Optional[int] = None
    thumb: Optional["PhotoSize"] = None
