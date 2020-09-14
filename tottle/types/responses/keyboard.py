from abc import ABC, abstractmethod
from typing import List, Optional

from pydantic import BaseModel, Field

from ..responses.game import CallbackGame
from ..responses.login import LoginUrl


class AbstractMarkup(ABC, BaseModel):
    @abstractmethod
    def add_row(self, *buttons) -> "AbstractMarkup":
        pass

    @abstractmethod
    def add_buttons(self, *buttons) -> "AbstractMarkup":
        pass

    @abstractmethod
    def insert(self, button) -> "AbstractMarkup":
        pass


class KeyboardButtonPollType(BaseModel):
    type: Optional[str]


class KeyboardButton(BaseModel):
    text: str
    request_contact: Optional[bool] = False
    request_location: Optional[bool] = False


class InlineKeyboardButton(BaseModel):
    text: str
    url: Optional[str] = ""
    login_url: Optional[LoginUrl] = None

    pay: Optional[bool] = None

    callback_data: Optional[str] = ""
    callback_game: Optional[CallbackGame] = None

    switch_inline_query: Optional[str] = ""
    switch_inline_query_current_chat: Optional[str] = ""


class ReplyKeyboardRemove(BaseModel):
    remove_keyboard: bool = True
    selective: Optional[bool] = False


class ReplyKeyboardMarkup(AbstractMarkup):
    keyboard: List[List[KeyboardButton]] = []

    def add_row(self, *buttons: KeyboardButton) -> "ReplyKeyboardMarkup":
        button_array: List[KeyboardButton] = []

        for button in buttons:
            button_array.append(button)

        self.keyboard.append(button_array)

        return self

    def add_buttons(self, *buttons: KeyboardButton) -> "ReplyKeyboardMarkup":
        row: List[KeyboardButton] = []

        for index, button in enumerate(buttons, start=1):
            row.append(button)

            if index % 3 == 0:
                self.keyboard.append(row)
                row = []

        if len(row) > 0:
            self.keyboard.append(row)

        return self

    def insert(self, button: KeyboardButton) -> "ReplyKeyboardMarkup":
        if self.keyboard and len(self.keyboard[-1]) < 3:
            self.keyboard[-1].append(button)
        else:
            self.add_buttons(button)

        return self


class InlineKeyboardMarkup(AbstractMarkup):
    inline_keyboard: List[List[InlineKeyboardButton]] = []

    def add_row(self, *buttons: InlineKeyboardButton) -> "InlineKeyboardMarkup":
        button_array: List[InlineKeyboardButton] = []

        for button in buttons:
            button_array.append(button)

        self.inline_keyboard.append(button_array)

        return self

    def add_buttons(self, *buttons: InlineKeyboardButton) -> "InlineKeyboardMarkup":
        row: List[InlineKeyboardButton] = []

        for index, button in enumerate(buttons, start=1):
            row.append(button)

            if index % 3 == 0:
                self.inline_keyboard.append(row)
                row = []

        if len(row) > 0:
            self.inline_keyboard.append(row)

        return self

    def insert(self, button: InlineKeyboardButton) -> "InlineKeyboardMarkup":
        if self.inline_keyboard and len(self.inline_keyboard[-1]) < 3:
            self.inline_keyboard[-1].append(button)
        else:
            self.add_buttons(button)

        return self

