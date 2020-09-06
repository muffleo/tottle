from pydantic import BaseModel, Field
from typing import List, Optional

from tottle.types.objects.game import CallbackGame
from tottle.types.objects.login import LoginUrl
from tottle.types.objects.message import Message
from tottle.types.objects.user import User


class CallbackQuery(BaseModel):
    id: str
    sender: User = Field(alias="from")
    message: Optional[Message] = None
    inline_message_id: Optional[str] = ""

    chat_instance: str
    data: Optional[str] = ""
    game_short_name: Optional[str] = ""


class InlineKeyboardButton(BaseModel):
    text: str
    url: Optional[str] = ""
    login_url: Optional[LoginUrl] = None

    pay: Optional[bool] = None

    callback_data: Optional[str] = ""
    callback_game: Optional[CallbackGame] = None

    switch_inline_query: Optional[str] = ""
    switch_inline_query_current_chat: Optional[str] = ""


class InlineKeyboardMarkup(BaseModel):
    inline_keyboard: List[List[InlineKeyboardButton]] = []