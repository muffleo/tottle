import typing

from tottle.api import API
from tottle.dispatch.dispenser.abc import ABCStateDispenser
from tottle.dispatch.middlewares.abc import MiddlewareResponse
from tottle.tools.enums import EventType
from tottle.tools.dev_tools.logger import logger
from tottle.dispatch.handlers import ABCHandler
from tottle.dispatch.views.abc import ABCView
from tottle.dispatch.middlewares import BaseMiddleware
from tottle.types.minis.message import message_min


class MessageView(ABCView):
    handlers: typing.List["ABCHandler"] = []
    middlewares: typing.List["BaseMiddleware"] = []

    async def processor(self, event: dict) -> bool:
        return bool(event.get(EventType.MESSAGE))

    async def handler(
            self, event: dict, api: API, state_dispenser: "ABCStateDispenser"
    ) -> typing.Any:
        logger.debug("Handling update {} with message view", event.get("update_id"))

        context_variables = {}
        message = message_min(event, api)
        message.state_peer = await state_dispenser.cast(message.chat.id)

        for middleware in self.middlewares:
            response = await middleware.pre(message)
            if response == MiddlewareResponse(False):
                return []
            elif isinstance(response, dict):
                context_variables.update(response)

        handle_responses = []
        for handler in self.handlers:
            result = await handler.filter(message)

            if result is False:
                continue
            elif isinstance(result, dict):
                context_variables.update(result)

            handler_response = await handler.process(message, **context_variables)
            handle_responses.append(handler_response)

        for middleware in self.middlewares:
            await middleware.post(message, self, handle_responses)
