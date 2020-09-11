import typing
from abc import ABC, abstractmethod

from tottle.types.methods import *

if typing.TYPE_CHECKING:
    from tottle.api import API


class APICategories(ABC):
    @property
    def messages(self) -> message.MessageCategory:
        return message.MessageCategory(self.instance)

    @property
    def users(self) -> user.UserCategory:
        return user.UserCategory(self.instance)

    @property
    @abstractmethod
    def instance(self) -> "API":
        pass
