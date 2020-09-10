import asyncio
import sys
import typing

from loguru import logger

from tottle.api import API
from tottle.polling.labelers.bot import BotLabeler
from tottle.polling.polling import Polling
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

        self.on: "BotLabeler" = BotLabeler()
        self.polling: "Polling" = Polling(self.api)
        self.loop = loop or asyncio.get_event_loop()

        if uvloop is not None:
            asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

        logger.remove()
        logger.add(
            level=0,
            enqueue=True,
            sink=sys.stdout,
            format="<level>/ Tottle / {message}</level>"
                   " [at <light-blue><bold>{time:HH:MM:ss}</bold></light-blue>]",
            colorize=True,
            filter=LoggerLevel(logging_level),
        )

        logger.level("INFO", color="<blue>")
        logger.level("SUCCESS", color="<green>")
        logger.level("WARNING", color="<yellow>")
        logger.level("ERROR", color="<red>")
        logger.level("DEBUG", color="<white>")

    def run_polling(self):
        logger.info("Polling will be started. Is it ok?")

        try:
            self.loop.create_task(self.polling.run())
            self.loop.run_forever()
        except KeyboardInterrupt:
            logger.warning("Keyboard interrupt...")
