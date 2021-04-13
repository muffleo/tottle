import typing
from abc import ABC, abstractmethod

from tottle.http import ABCSessionManager


class ABCAPI(ABC):
    http: ABCSessionManager

    @abstractmethod
    async def request(
        self,
        method: str,
        data: typing.Optional[dict] = None,
    ) -> typing.Optional[typing.Any]:
        pass
