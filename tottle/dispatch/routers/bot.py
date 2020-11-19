from tottle.api import API
from tottle.dispatch.dispenser.abc import ABCStateDispenser
from tottle.dispatch.routers.abc import ABCRouter
from tottle.dispatch.views import ABCView, MessageView

from typing import Dict


class BotRouter(ABCRouter):
    views = {"message": MessageView()}

    async def route(self, event: dict, api: "API"):
        for view in self.views.values():
            if not await view.processor(event):
                continue
            return await view.handler(event, api, self.state_dispenser)

    def construct(
        self, views: Dict[str, "ABCView"], state_dispenser: ABCStateDispenser
    ) -> "BotRouter":
        self.views = views
        self.state_dispenser = state_dispenser
        return self
