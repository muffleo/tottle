import typing
from abc import ABC, abstractmethod

from tottle import API
from tottle.dispatch.handlers import ABCHandler
from tottle.types.responses.update import Update


class ABCView(ABC):
    handlers: typing.List["ABCHandler"]

    @abstractmethod
    async def processor(self, event: Update) -> bool:
        pass

    @abstractmethod
    async def handler(self, event: Update, api: API) -> typing.Any:
        pass
