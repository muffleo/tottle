from typing import Optional

from pydantic import BaseModel

from tottle.types.responses.mask import MaskPosition
from tottle.types.responses.photo import PhotoSize


class Sticker(BaseModel):
    file_id: str
    file_unique_id: str
    file_size: Optional[int] = 0

    width: int
    height: int

    is_animated: bool
    thumb: Optional[PhotoSize] = None

    emoji: Optional[str] = None
    set_name: Optional[str] = None
    mask_position: Optional[MaskPosition] = None
