from tottle.api import API, ABCAPI
from tottle.dispatch.dispenser.default import DefaultStateDispenser
from tottle.framework.bot.labelers import BotLabeler, ABCBotLabeler
from tottle.framework.abc import ABCFramework
from tottle.polling import BotPolling, ABCPolling
from tottle.dispatch.routers import BotRouter, ABCRouter
from tottle.tools.dev_tools.loop_wrapper.loop_wrapper import LoopWrapper
from tottle.tools.dev_tools.logger import Logger, logger, default_logger
from tottle.exception_factory import ABCErrorHandler, ErrorHandler

from typing import Callable, Optional, NoReturn, Iterable
from asyncio import AbstractEventLoop, get_event_loop, set_event_loop_policy

try:
    import uvloop

    set_event_loop_policy(uvloop.EventLoopPolicy())
except ImportError:
    ...


class Bot(ABCFramework):
    def __init__(
        self,
        token: Optional[str] = None,
        api: Optional[ABCAPI] = None,
        polling: Optional[ABCPolling] = None,
        router: Optional["ABCRouter"] = None,
        labeler: Optional["ABCBotLabeler"] = None,
        loop: Optional[AbstractEventLoop] = None,
        loop_wrapper: Optional[LoopWrapper] = None,
        custom_logger: Optional[Logger] = None,
        task_each_event: bool = False,
        error_handler: Optional["ABCErrorHandler"] = None,
    ):
        self.api: "API" = API(token) if token else api
        self.apis: Optional[Iterable["ABCAPI"]] = None
        self.error_handler = error_handler or ErrorHandler()
        self.loop_wrapper: "LoopWrapper" = loop_wrapper or LoopWrapper()
        self.labeler: "BotLabeler" = labeler or BotLabeler()
        self.state_dispenser = DefaultStateDispenser()
        self.task_each_event = task_each_event
        self._router: "BotRouter" = router or BotRouter()
        self._polling: "BotPolling" = polling or BotPolling(self.api)
        self._loop = loop

        (custom_logger or default_logger).setup()

    async def run_polling(
        self, custom_polling: Optional[ABCPolling] = None, apis_count: int = 0
    ) -> NoReturn:
        polling = custom_polling or self.polling
        logger.info("Polling will be started!")

        async for update in polling.listen():  # type: ignore
            logger.debug("New update: {}", update)

            if self.apis:
                self.api = self.apis[apis_count]

            if not self.task_each_event:
                await self.router.route(update, self.api)
            else:
                self.loop.create_task(self.router.route(update, self.api))

    def run_forever(
        self,
        on_startup: Optional[Callable] = None,
        on_shutdown: Optional[Callable] = None,
    ):
        lw = LoopWrapper(on_startup=on_startup, on_shutdown=on_shutdown)
        lw.add_task(self.run_polling())
        lw.run_forever()

    @property
    def on(self) -> "ABCBotLabeler":
        return self.labeler

    @property
    def polling(self) -> "ABCPolling":
        return self._polling.construct(self.api)

    @property
    def router(self) -> "ABCRouter":
        return self._router.construct(
            views=self.labeler.views(),
            state_dispenser=self.state_dispenser,
            error_handler=self.error_handler,
        )

    @property
    def loop(self) -> AbstractEventLoop:
        if self._loop is None:
            self._loop = get_event_loop()
        return self._loop

    @loop.setter
    def loop(self, new_loop: AbstractEventLoop):
        self._loop = new_loop

    @router.setter
    def router(self, new_router: "ABCRouter"):
        self._router = new_router

    @polling.setter
    def polling(self, value):
        self._polling = value
