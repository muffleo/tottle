from typing import Any, Dict, List, NamedTuple, Callable
from loguru import logger

from tottle.tools.enums import EventType
from tottle.dispatch.dispenser.abc import ABCStateDispenser
from tottle.dispatch.handlers import ABCHandler
from tottle.dispatch.middlewares import BaseMiddleware, MiddlewareResponse
from tottle.dispatch.return_manager.bot import BotMessageReturnHandler
from tottle.dispatch.views.abc import ABCView
from tottle import API

HandlerBasement = NamedTuple(
    "HandlerBasement", [("dataclass", Callable), ("handler", ABCHandler)]
)


class RawEventView(ABCView):
    def __init__(self):
        self.handlers: Dict[EventType, HandlerBasement] = {}
        self.middlewares: List["BaseMiddleware"] = []
        self.handler_return_manager = BotMessageReturnHandler()

    async def processor(self, event: dict) -> bool:
        for i in EventType:
            if not event.get(i.value):
                continue

            return True

        return False

    async def handler(
        self, event: dict, api: API, state_dispenser: "ABCStateDispenser"
    ) -> Any:
        logger.debug("Handling event ({}) with RawEvent view".format(event.get("update_id")))

        context_variables = {}
        handle_responses = []

        for middleware in self.middlewares:
            response = await middleware.pre(event)

            if response == MiddlewareResponse(False):
                return []
            elif isinstance(response, dict):
                context_variables.update(response)

        for k, handler in self.handlers.items():
            result = False

            for _ in EventType:
                if not event.get(k):
                    continue

                result = True
                break

            if result is False:
                continue
            elif isinstance(result, dict):
                context_variables.update(result)

            handler_response = await handler.handler.process(event, **context_variables)
            handle_responses.append(handler_response)
            return_handler = self.handler_return_manager.get_handler(handler_response)

            if return_handler is not None:
                await return_handler(
                    self.handler_return_manager,
                    handler_response,
                    event,
                    context_variables,
                )

            if handler.handler.blocking:
                break

        for middleware in self.middlewares:
            await middleware.post(event, self, handle_responses, [i["handler"] for i in self.handlers])
