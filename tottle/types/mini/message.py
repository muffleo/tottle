import typing

from tottle.api import API
from ..responses.chat import Message
from ..responses.update import Update


class MessageMini(Message):
    ctx_api: typing.Optional[typing.Any] = None

    @property
    def api(self) -> "API":
        return getattr(self, "ctx_api")

    async def answer(
            self,
            text: str,
            parse_mode: typing.Optional[str] = None,
            disable_web_page_preview: typing.Optional[bool] = None,
            disable_notification: typing.Optional[bool] = None,
            reply_markup: typing.Optional[dict] = None,
    ) -> Message:
        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        params["chat_id"] = self.chat.id

        return await self.api.messages.send_message(**params)

    async def reply(
            self,
            text: str,
            parse_mode: typing.Optional[str] = None,
            disable_web_page_preview: typing.Optional[bool] = None,
            disable_notification: typing.Optional[bool] = None,
            reply_markup: typing.Optional[dict] = None,
    ) -> Message:
        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        params["chat_id"] = self.chat.id
        params["reply_to_message_id"] = self.message_id

        return await self.api.messages.send_message(**params)

    async def forward(
            self,
            chat_id: typing.Union[int, str],
            disable_notification: typing.Optional[bool] = None,
    ) -> Message:
        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        params["from_chat_id"] = self.chat.id
        params["message_id"] = self.message_id

        return await self.api.messages.forward_message(**params)


def message_min(event: dict, api: "API") -> "MessageMini":
    update = Update(**event)
    message = MessageMini(
        **update.message.dict()
    )
    setattr(message, "ctx_api", api)
    return message
