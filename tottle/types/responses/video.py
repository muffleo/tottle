from typing import Optional

from pydantic import BaseModel

from tottle.types.responses.photo import PhotoSize


class Video(BaseModel):
    file_id: str
    file_unique_id: str
    file_size: Optional[int] = None

    width: int
    height: int
    duration: int

    thumb: Optional[PhotoSize] = None
    mime_type: Optional[str] = None


class VideoNote(BaseModel):
    file_id: str
    file_unique_id: str
    file_size: Optional[int] = None

    length: int
    duration: int
    thumb: Optional[PhotoSize] = None
