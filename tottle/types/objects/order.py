from pydantic import BaseModel
from typing import Optional


class ShippingAddress(BaseModel):
    country_code: str
    state: str
    city: str
    street_line1: str
    street_line2: str
    post_code: str


class OrderInfo(BaseModel):
    name: Optional[str] = ""
    phone_number: Optional[str] = ""
    email: Optional[str] = ""
    shipping_address: Optional[ShippingAddress] = None
