from pydantic import BaseModel
from typing import Optional


class MaskPosition(BaseModel):
    point: str

    x_shift: float
    y_shift: float
    scale: float
