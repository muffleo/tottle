from typing import List, Optional

from pydantic import BaseModel, Field

from ..objects import game, login, user


class CallbackQuery(BaseModel):
    id: str
    sender: "user.User" = Field(alias="from")
    message: Optional["message.Message"] = None
    inline_message_id: Optional[str] = ""

    chat_instance: str
    data: Optional[str] = ""
    game_short_name: Optional[str] = ""


class InlineKeyboardButton(BaseModel):
    text: str
    url: Optional[str] = ""
    login_url: Optional["login.LoginUrl"] = None

    pay: Optional[bool] = None

    callback_data: Optional[str] = ""
    callback_game: Optional["game.CallbackGame"] = None

    switch_inline_query: Optional[str] = ""
    switch_inline_query_current_chat: Optional[str] = ""


class InlineKeyboardMarkup(BaseModel):
    inline_keyboard: List[List["InlineKeyboardButton"]] = []
