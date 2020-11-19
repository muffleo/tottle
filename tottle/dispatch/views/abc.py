import typing
from abc import ABC, abstractmethod

from tottle import API
from tottle.dispatch.middlewares import BaseMiddleware
from tottle.dispatch.handlers import ABCHandler
from tottle.dispatch.dispenser.abc import ABCStateDispenser


class ABCView(ABC):
    handlers: typing.List["ABCHandler"]
    middlewares: typing.List["BaseMiddleware"]

    @abstractmethod
    async def processor(self, event: dict) -> bool:
        pass

    @abstractmethod
    async def handler(
            self, event: dict, api: API, state_dispenser: "ABCStateDispenser"
    ) -> typing.Any:
        pass

    def register_middleware(self, middleware: "BaseMiddleware"):
        self.middlewares.append(middleware)
