from loguru import logger

from tottle.api import API
from tottle.dispatch.dispenser.abc import ABCStateDispenser
from tottle.dispatch.routers.abc import ABCRouter
from tottle.dispatch.views import ABCView, MessageView

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
                raise e

    def construct(
        self, views: Dict[str, "ABCView"], state_dispenser: ABCStateDispenser
    ) -> "BotRouter":
        self.views = views
        self.state_dispenser = state_dispenser
        return self
