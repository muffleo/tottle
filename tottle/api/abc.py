import typing
from abc import ABC, abstractmethod

from tottle.http import ABCSessionManager


class ABCAPI(ABC):
    http: ABCSessionManager

    @abstractmethod
    async def request(
            self,
            method: str,
            params: typing.Optional[dict] = None,
    ) -> dict:
        pass
