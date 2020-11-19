from typing import Optional

from pydantic import BaseModel

from tottle.types.responses.photo import PhotoSize


class Animation(BaseModel):
    file_id: str
    file_unique_id: str
    width: int
    height: int
    duration: int
    thumb: Optional["PhotoSize"] = None
    file_name: Optional[str] = None
    mime_type: Optional[str] = None
    file_size: Optional[int] = None
