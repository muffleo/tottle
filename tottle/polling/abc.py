from abc import ABC, abstractmethod
from typing import AsyncIterator, Any

from tottle.api import ABCAPI


class ABCPolling(ABC):
    @abstractmethod
    async def get_updates(self) -> Any:
        pass

    @abstractmethod
    async def listen(self) -> AsyncIterator[dict]:
        pass

    @property
    @abstractmethod
    def api(self) -> "ABCAPI":
        pass

    @api.setter
    def api(self, new_api: "ABCAPI"):
        pass

    @abstractmethod
    def construct(self, api: "ABCAPI") -> "ABCPolling":
        pass
