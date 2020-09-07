import typing

from .base import Base
from ..objects import chat, keyboard, user


class BotCategory(Base):
    async def get_me(self, **kwargs) -> user.User:
        params = self.get_set_params(locals())
        return user.User(
            **await self.api.request(
                "getMe", params
            )
        )

    async def send_message(
            self,
            text: str,
            chat_id: typing.Union[int, str],
            parse_mode: typing.Optional[str] = None,
            disable_web_page_preview: typing.Optional[bool] = None,
            disable_notification: typing.Optional[bool] = None,
            reply_to_message_id: typing.Optional[int] = None,
            reply_markup: typing.Optional[keyboard.InlineKeyboardMarkup] = None,
            **kwargs
    ) -> chat.Message:
        params = self.get_set_params(locals())
        return chat.Message(
            **await self.api.request(
                "sendMessage", params
            )
        )

    async def forward_message(
            self,
            message_id: int,
            chat_id: typing.Union[int, str],
            from_chat_id: typing.Union[int, str],
            disable_notification: typing.Optional[bool] = None,
            **kwargs
    ) -> chat.Message:
        params = self.get_set_params(locals())
        return chat.Message(
            **await self.api.request(
                "forwardMessage", params
            )
        )
