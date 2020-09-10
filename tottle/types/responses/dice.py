from pydantic import BaseModel


class Dice(BaseModel):
    emoji: str
    value: int
