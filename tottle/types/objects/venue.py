from pydantic import BaseModel
from typing import Optional

from tottle.types.objects.location import Location


class Venue(BaseModel):
    location: Location

    title: str
    address: str
    foursquare_id: Optional[str] = ""
    foursquare_type: Optional[str] = ""
