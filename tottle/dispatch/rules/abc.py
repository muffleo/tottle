from abc import ABC, abstractmethod
from typing import Union, Type

from tottle.types.responses.chat import Message
from tottle.types.responses.update import Update


class ABCRule(ABC):
    config: dict = {}

    @classmethod
    def with_config(cls, config) -> Type["ABCRule"]:
        cls.config = config
        return cls

    @abstractmethod
    async def check(self, event: Union[Update, Message]):
        pass
