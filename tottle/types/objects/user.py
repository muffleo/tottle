from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    id: int
    is_bot: bool
    first_name: str
    last_name: Optional[str] = ""
    username: Optional[str] = ""
    language_code: Optional[str] = ""
    can_join_groups: Optional[bool] = None
    can_read_all_group_messages: Optional[bool] = None
    supports_inline_queries: Optional[bool] = None

