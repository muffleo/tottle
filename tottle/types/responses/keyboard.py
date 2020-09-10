from typing import List, Optional

from pydantic import BaseModel

from ..responses.game import CallbackGame
from ..responses.login import LoginUrl


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
