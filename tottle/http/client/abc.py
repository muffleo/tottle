import typing
from abc import ABC, abstractmethod


class ABCHTTPClient(ABC):
    @abstractmethod
    async def request_text(
            self, method: str, url: str, data: typing.Optional[dict] = None, **kwargs
    ) -> str:
        pass

    @abstractmethod
    async def request_json(
            self, method: str, url: str, data: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        pass

    @abstractmethod
    async def request_content(
            self, method: str, url: str, data: typing.Optional[dict] = None, **kwargs
    ) -> bytes:
        pass

    @abstractmethod
    async def close(self) -> typing.NoReturn:
        pass

    async def __aenter__(self) -> "ABCHTTPClient":
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> typing.NoReturn:
        await self.close()
