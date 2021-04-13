import typing
from abc import ABC, abstractmethod

from tottle import API
from tottle.dispatch.middlewares import BaseMiddleware
from tottle.dispatch.handlers import ABCHandler
from tottle.dispatch.dispenser.abc import ABCStateDispenser
from tottle.dispatch.return_manager import BaseReturnManager


class ABCView(ABC):
    handlers: typing.List["ABCHandler"]
    middlewares: typing.List["BaseMiddleware"]
    handler_return_manager: BaseReturnManager

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

    def __repr__(self) -> str:
        return (
            f"<{self.__class__.__name__} "
            f"handlers={self.handlers} "
            f"middlewares={self.middlewares} "
            f"handler_return_manager={self.handler_return_manager}"
        )
