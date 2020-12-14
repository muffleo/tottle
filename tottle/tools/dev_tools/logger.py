import sys
from typing import Union, TextIO, Callable, Iterable, Optional

from loguru import logger
from loguru._handler import Message, Handler


class LoggerLevel:
    def __init__(self, level):
        self.level = level

    def __call__(self, record):
        level_no = logger.level(self.level).no
        return record["level"].no >= level_no


class Logger:
    def __init__(
            self,
            format: str,
            enqueue: bool = True,
            levels: Optional[Iterable[dict]] = None,
            current_level: Optional[LoggerLevel] = None,
            sink: Optional[Union[TextIO, Callable[[Message], None], Handler]] = None,
    ):
        self.format = format
        self.enqueue = enqueue
        self.levels = levels or []
        self.current_level = current_level or LoggerLevel("DEBUG")
        self.sink = sink or sys.stdout

    def setup(self):
        logger.remove()
        logger.add(
            level=0,
            enqueue=self.enqueue,
            sink=self.sink,
            format=self.format,
            colorize=True,
            filter=self.current_level,
        )

        for level in self.levels:
            for k, v in level.items():
                logger.level(k, **v)


default_logger = Logger(
        format="<level>Tottle / {message}</level>"
               " [at <light-blue><bold>{time:HH:MM:ss}</bold></light-blue>]",
        levels=[
            {"INFO": {"color": "<blue>"}},
            {"SUCCESS": {"color": "<green>"}},
            {"WARNING": {"color": "<yellow>"}},
            {"ERROR": {"color": "<red>"}},
            {"DEBUG": {"color": "<white>"}}
        ]
    )
