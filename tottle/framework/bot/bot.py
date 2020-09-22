import asyncio
import sys

from typing import Callable, Optional
from loguru import logger

from tottle.api import API
from tottle.dispatch.labelers import BotLabeler
from tottle.framework.polling import Polling
from tottle.dispatch.routers import BotRouter
from tottle.http import SessionManager, AiohttpClient, ABCSessionManager
from tottle.utils.logger import LoggerLevel
from tottle.utils.taskmanager import TaskManager

try:
    import uvloop
except ImportError:
    uvloop = None


class Bot:
    def __init__(
            self,
            token: str,
            logging_level: Optional[str] = "INFO",
            loop: Optional[asyncio.AbstractEventLoop] = None,
            session_manager: Optional[ABCSessionManager] = None,
    ):

        self.loop = loop or asyncio.get_event_loop()
        self.http = session_manager or SessionManager(AiohttpClient)

        self.token = token
        self.api: "API" = API(self.token, self.http)

        self.on: "BotLabeler" = BotLabeler()
        self.router: "BotRouter" = BotRouter()
        self.polling: "Polling" = Polling(self.api, self.router)

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

    def run_polling(
            self,
            on_startup: Optional[Callable] = None,
            on_shutdown: Optional[Callable] = None,
    ):
        logger.info("Polling will be started")

        manager = TaskManager(
            self.loop,
            on_startup=on_startup,
            on_shutdown=on_shutdown,
        )
        manager.add_task(self.polling.run())
        manager.run()
