from typing import Optional

from pydantic import BaseModel

from tottle.types.responses.location import Location


class Venue(BaseModel):
    location: Location

    title: str
    address: str
    foursquare_id: Optional[str] = None
    foursquare_type: Optional[str] = None
