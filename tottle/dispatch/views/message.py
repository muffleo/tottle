from typing import List, Callable, Any, Optional

from tottle.api import API
from tottle.dispatch.dispenser.abc import ABCStateDispenser
from tottle.dispatch.middlewares.abc import MiddlewareResponse
from tottle.tools.enums import EventType
from tottle.tools.dev_tools.logger import logger
from tottle.dispatch.handlers import ABCHandler
from tottle.dispatch.views.abc import ABCView
from tottle.dispatch.middlewares import BaseMiddleware
from tottle.types.minis.message import message_min


DEFAULT_STATE_KEY = "id"


class MessageView(ABCView):
    def __init__(self):
        self.state_source_key = DEFAULT_STATE_KEY
        self.handlers: List["ABCHandler"] = []
        self.middlewares: List["BaseMiddleware"] = []
        self.default_text_approximators: List[Callable[[message_min], str]] = []

    async def processor(self, event: dict) -> bool:
        return bool(event.get(EventType.MESSAGE))

    def get_state_key(self, event: dict) -> Optional[int]:
        return event["message"]["from"].get(self.state_source_key)

    async def handler(
            self, event: dict, api: API, state_dispenser: "ABCStateDispenser"
    ) -> Any:
        logger.debug("Handling update {} with message view", event.get("update_id"))

        context_variables = {}
        message = message_min(event, api)
        message.state_peer = await state_dispenser.cast(self.get_state_key(event))

        for text_ax in self.default_text_approximators:
            message.text = text_ax(message)

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

            if handler.blocking:
                break

        for middleware in self.middlewares:
            await middleware.post(message, self, handle_responses, self.handlers)