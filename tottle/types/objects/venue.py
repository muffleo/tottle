from typing import Optional

from pydantic import BaseModel

from ..objects.location import Location


class Venue(BaseModel):
    location: Location

    title: str
    address: str
    foursquare_id: Optional[str] = ""
    foursquare_type: Optional[str] = ""
