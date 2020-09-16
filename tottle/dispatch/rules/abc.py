from abc import ABC, abstractmethod
from typing import Union

from tottle.types.responses.chat import Message
from tottle.types.responses.update import Update


class ABCRule(ABC):
    @abstractmethod
    async def check(self, event: Union[Update, Message]):
        pass
