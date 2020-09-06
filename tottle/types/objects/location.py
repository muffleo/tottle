from pydantic import BaseModel
from typing import Optional


class Location(BaseModel):
    longitude: float
    latitude: float
