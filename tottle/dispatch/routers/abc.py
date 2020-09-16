import typing
from abc import ABC, abstractmethod

from tottle.api import ABCAPI
from ..views import ABCView


class ABCRouter(ABC):
    views: typing.Dict[str, "ABCView"]

    @abstractmethod
    async def route(self, event: dict, api: "ABCAPI") -> typing.Any:
        pass

    def add_view(self, name: str, tree: "ABCView") -> typing.NoReturn:
        self.views[name] = tree

    def view(self, name: str) -> typing.Callable[..., typing.Type["ABCView"]]:
        def decorator(view: typing.Type["ABCView"]):
            self.add_view(name, view())
            return view

        return decorator
