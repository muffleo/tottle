from tottle.api import API
from tottle.types.responses.update import Update
from .abc import ABCRouter
from ..views import MessageView


class BotRouter(ABCRouter):
    views = {"message": MessageView()}

    async def route(self, event: Update, api: "API"):
        for view in self.views.values():
            if not await view.processor(event):
                continue
            return await view.handler(event, api)
