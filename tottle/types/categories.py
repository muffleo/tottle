import typing
from abc import ABC, abstractmethod

from tottle.types.methods import *

if typing.TYPE_CHECKING:
    from tottle.api import API


class APICategories(ABC):
    @property
    def bot(self) -> bot.BotCategory:
        return bot.BotCategory(self.instance)

    @property
    @abstractmethod
    def instance(self) -> "API":
        pass
