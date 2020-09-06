from pydantic import BaseModel
from typing import Optional


class LoginUrl(BaseModel):
    url: str
    forward_text: Optional[str] = ""
    bot_username: Optional[str] = ""
    request_write_access: Optional[bool] = None
