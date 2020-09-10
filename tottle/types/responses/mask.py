from pydantic import BaseModel


class MaskPosition(BaseModel):
    point: str

    x_shift: float
    y_shift: float
    scale: float
