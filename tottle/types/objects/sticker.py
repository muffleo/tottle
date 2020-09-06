from pydantic import BaseModel
from typing import Optional

from tottle.types.objects.mask import MaskPosition
from tottle.types.objects.photo import PhotoSize


class Sticker(BaseModel):
    file_id: str
    file_unique_id: str
    file_size: Optional[int] = 0

    width: int
    height: int

    is_animated: bool
    thumb: Optional[PhotoSize] = None

    emoji: Optional[str] = ""
    set_name: Optional[str] = ""
    mask_position: Optional[MaskPosition]
