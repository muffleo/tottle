import typing
from abc import ABC, abstractmethod


class ABCHandler(ABC):
    blocking: bool = False

    @abstractmethod
    async def filter(self, event: typing.Any) -> typing.Union[dict, bool]:
        pass

    @abstractmethod
    async def process(self, event: typing.Any, **context) -> typing.Any:
        pass
