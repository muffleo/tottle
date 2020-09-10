from pydantic import BaseModel


class Location(BaseModel):
    longitude: float
    latitude: float
