from tottle.framework.abc_blueprint import ABCBlueprint
from tottle.framework.bot.labelers import BotLabeler
from tottle.framework.bot.bot import Bot
from tottle.api import ABCAPI, API
from tottle.polling import ABCPolling
from tottle.dispatch import BotRouter

from loguru import logger
from typing import Optional


class BotBlueprint(ABCBlueprint):
    def __init__(
            self,
            name: Optional[str] = None,
            labeler: Optional[BotLabeler] = None,
            router: Optional[BotRouter] = None,
    ):
        if name is not None:
            self.name = name

        self.labeler = labeler or BotLabeler()
        self.router: BotRouter = router or BotRouter()
        self.constructed = False

    def construct(self, api: ABCAPI, polling: ABCPolling) -> "BotBlueprint":
        self.api = api
        self.polling = polling
        self.constructed = True
        return self

    def load(self, framework: "Bot") -> "BotBlueprint":
        framework.labeler.load(self.labeler)  # type: ignore
        logger.debug(f"Blueprint {self.name!r} loaded")
        return self.construct(framework.api, framework.polling)

    @property
    def on(self) -> BotLabeler:
        return self.labeler
