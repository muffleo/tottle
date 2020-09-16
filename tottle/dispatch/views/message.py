import typing

from tottle.api import API
from tottle.utils.enums import EventType
from tottle.utils.logger import logger
from ..handlers import ABCHandler
from ..views.abc import ABCView
from ...types.mini import message_min


class MessageView(ABCView):
    handlers: typing.List["ABCHandler"] = []

    async def processor(self, event: dict) -> bool:
        return bool(event.get(EventType.MESSAGE))

    async def handler(self, event: dict, api: API) -> typing.Any:
        message = message_min(event, api)

        handle_responses = []
        for handler in self.handlers:
            result = await handler.filter(message)

            if result is False:
                continue
            elif not isinstance(result, dict):
                result = {}

            handle_responses.append(
                await handler.process(
                    message, **result
                )
            )

            logger.success(
                "Message \"{}\" was processed successfully!",
                message.text.replace(
                    "\n", " "
                )
            )

        return handle_responses
