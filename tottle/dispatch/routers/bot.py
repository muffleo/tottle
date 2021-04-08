from loguru import logger

from tottle.api import API
from tottle.dispatch.dispenser.abc import ABCStateDispenser
from tottle.dispatch.routers.abc import ABCRouter
from tottle.dispatch.views import ABCView, MessageView
from tottle.exception_factory import ABCErrorHandler

from typing import Dict


class BotRouter(ABCRouter):
    views = {"message": MessageView()}

    async def route(self, event: dict, api: "API"):
        logger.debug("Routing update {}".format(event))

        for view in self.views.values():
            try:
                if not await view.processor(event):
                    continue
                await view.handler(event, api, self.state_dispenser)
            except BaseException as e:
                await self.error_handler.handle(e)

    def construct(
        self,
        views: Dict[str, "ABCView"],
        state_dispenser: ABCStateDispenser,
        error_handler: ABCErrorHandler,
    ) -> "BotRouter":
        self.views = views
        self.state_dispenser = state_dispenser
        self.error_handler = error_handler
        return self
