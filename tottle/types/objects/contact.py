from pydantic import BaseModel
from typing import Optional


class Contact(BaseModel):
    phone_number: str
    first_name: str
    last_name: Optional[str] = ""
    user_id: Optional[int] = 0
    vcard: Optional[str] = ""
