import typing
from abc import ABC, abstractmethod


class Constructor(ABC):
    @abstractmethod
    def construct(self, *args, **kwargs) -> typing.ClassVar:
        """ Construct new object """
        pass
