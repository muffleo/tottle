import typing
from abc import ABC, abstractmethod

from tottle.api import ABCAPI
from ..views import ABCView


class ABCRouter(ABC):
    trees: typing.Dict[str, "ABCView"]

    @abstractmethod
    async def route(self, event: dict, api: "ABCAPI") -> typing.Any:
        pass

    def add_view(self, name: str, tree: "ABCView") -> typing.NoReturn:
        self.trees[name] = tree

    def tree(self, name: str) -> typing.Callable[..., typing.Type["ABCView"]]:
        def decorator(tree: typing.Type["ABCView"]):
            self.add_view(name, tree())
            return tree

        return decorator
