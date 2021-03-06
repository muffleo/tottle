from .delayed_task import delayed_task
from .auto_reload import watch_to_reload

from asyncio import AbstractEventLoop, get_event_loop, iscoroutine, iscoroutinefunction
from typing import Optional, List, Coroutine, Any, Union, Callable, Iterable
from loguru import logger

Task = Coroutine[Any, Any, Any]


class LoopWrapper:
    def __init__(
        self,
        *,
        on_startup: Optional[List[Task]] = None,
        on_shutdown: Optional[List[Task]] = None,
        auto_reload: Optional[bool] = None,
        auto_reload_dir: Optional[str] = None,
        tasks: Optional[List[Task]] = None,
    ):
        self.on_startup = on_startup or []
        self.on_shutdown = on_shutdown or []
        self.auto_reload = auto_reload or False
        self.auto_reload_dir = auto_reload_dir or "."
        self.tasks = tasks or []

    def run_forever(self, loop: Optional[AbstractEventLoop] = None):
        loop = loop or get_event_loop()

        if not len(self.tasks):
            logger.warning("You ran loop with 0 tasks. Is it ok?")

        if not isinstance(self.on_startup, Iterable):
            self.on_startup = list(self.on_startup)

        try:
            [loop.run_until_complete(startup_task) for startup_task in self.on_startup]

            if self.auto_reload:
                loop.create_task(watch_to_reload(self.auto_reload_dir))

            for task in self.tasks:
                loop.create_task(task)

            loop.run_forever()
        except KeyboardInterrupt:
            logger.warning("Keyboard Interrupt")
        finally:
            [
                loop.run_until_complete(shutdown_task)
                for shutdown_task in self.on_shutdown
            ]

            if loop.is_running():
                loop.close()

    def add_task(self, task: Union[Task, Callable[..., Task]]):
        if iscoroutinefunction(task):  # type: ignore
            self.tasks.append(task())  # type: ignore
        elif iscoroutine(task):  # type: ignore
            self.tasks.append(task)  # type: ignore
        else:
            raise TypeError("Task should be coroutine or coroutine function")

    def interval(
        self, seconds: int = 0, minutes: int = 0, hours: int = 0, days: int = 0
    ) -> Callable[[Callable], Callable]:
        """A tiny template to wrap repeated tasks with decorator
        >>> lw = LoopWrapper()
        >>> @lw.interval(seconds=5)
        >>> async def repeated_function():
        >>>     print("This will be logged every five seconds")
        >>> lw.run_forever()
        """

        seconds += minutes * 60
        seconds += hours * 60 * 60
        seconds += days * 24 * 60 * 60

        def decorator(func: Callable):
            self.add_task(delayed_task(seconds, func))
            return func

        return decorator

    def timer(
        self, seconds: int = 0, minutes: int = 0, hours: int = 0, days: int = 0
    ) -> Callable[[Callable], Callable]:
        """A tiny template to wrap tasks with timer
        >>> lw = LoopWrapper()
        >>> @lw.timer(seconds=5)
        >>> async def delayed_function():
        >>>     print("This will after 5 seconds")
        >>> lw.run_forever()
        """
        seconds += minutes * 60
        seconds += hours * 60 * 60
        seconds += days * 24 * 60 * 60

        def decorator(func: Callable):
            self.add_task(delayed_task(seconds, func, do_break=True))
            return func

        return decorator
