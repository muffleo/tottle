from pydantic import BaseModel
from typing import Optional

from tottle.types.objects.message import Message
from tottle.types.objects.photo import ChatPhoto


class ChatPermissions(BaseModel):
    can_send_messages: Optional[bool] = None
    can_send_media_messages: Optional[bool] = None
    can_send_polls: Optional[bool] = None
    can_send_other_messages: Optional[bool] = None
    can_add_web_page_previews: Optional[bool] = None
    can_change_info: Optional[bool] = None
    can_invite_users: Optional[bool] = None
    can_pin_messages: Optional[bool] = None


class Chat(BaseModel):
    id: int
    type: str
    title: Optional[str] = ""
    username: Optional[str] = ""
    first_name: Optional[str] = ""
    last_name: Optional[str] = ""
    photo: Optional[ChatPhoto] = None
    description: Optional[str] = ""
    invite_link: Optional[str] = ""
    pinned_message: Optional[Message] = None

    permissions: Optional[ChatPermissions] = None
    slow_mode_delay: Optional[int] = 0
    sticker_set_name: Optional[str] = ""
    can_set_sticker_set: Optional[bool] = None
