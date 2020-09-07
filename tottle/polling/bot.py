import asyncio
import sys
import typing

from loguru import logger

from tottle.api import API
from tottle.utils.logger import LoggerLevel

try:
    import uvloop
except ImportError:
    uvloop = None


class Bot:
    def __init__(
            self,
            token: str,
            logging_level: str = "INFO",
            loop: typing.Optional[asyncio.AbstractEventLoop] = None,
    ):
        self.token = token
        self.api: "API" = API(self.token)

        self.polling_stopped: bool = True
        self.loop = loop or asyncio.get_event_loop()

        if uvloop is not None:
            asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

        self._setup_logger(logging_level)

    def run_polling(self):
        logger.warning("Polling will be started.. But is it OK?")
        self.loop.run_until_complete(self.run())

    async def run(self):
        offset = 0
        self.polling_stopped = False

        while not self.polling_stopped:
            updates = await self.api.request(
                "getUpdates", {
                    "offset": offset
                }
            )

            if updates:
                logger.debug(updates)
                offset = updates[-1]["update_id"] + 1

    def _setup_logger(self, level: str):
        logger.remove()
        logger.add(
            level=0,
            enqueue=False,
            sink=sys.stdout,
            format="<level><magenta>/ Tottle /</magenta> {message}</level>"
                   " [at <blue><bold>{time:HH:MM:ss}</bold></blue>]",
            colorize=True,
            filter=LoggerLevel(level),
        )

        logger.level("INFO", color="<white>")
        logger.level("SUCCESS", color="<green>")
        logger.level("WARNING", color="<yellow>")
        logger.level("ERROR", color="<red>")
        logger.level("DEBUG", color="<light-cyan>")
