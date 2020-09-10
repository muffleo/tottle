import typing

from tottle.api import API
from tottle.types.responses.update import Update
from tottle.utils.enums import EventType
from tottle.utils.logger import logger
from ..handlers import ABCHandler
from ..views.abc import ABCView


class MessageView(ABCView):
    handlers: typing.List["ABCHandler"] = []

    async def processor(self, event: Update) -> bool:
        if event.dict().get(EventType.MESSAGE):
            return True

    async def handler(self, event: Update, api: API) -> typing.Any:

        handle_responses = []

        for handler in self.handlers:
            result = await handler.filter(event)

            if result is False:
                continue
            elif not isinstance(result, dict):
                result = {}

            handle_responses.append(
                await handler.process(
                    event.message, **result
                )
            )

            logger.success(
                "Message \"{}\" is processed successfully!",
                event.message.text.replace(
                    "\n", " "
                )
            )

        return handle_responses
