import typing
from abc import ABC, abstractmethod

from tottle.api import ABCAPI
from tottle.dispatch.dispenser.abc import ABCStateDispenser
from tottle.dispatch.views import ABCView
from tottle.exception_factory import ABCErrorHandler


class ABCRouter(ABC):
    views: typing.Dict[str, "ABCView"]
    state_dispenser: ABCStateDispenser
    error_handler: ABCErrorHandler

    @abstractmethod
    async def route(self, event: dict, api: "ABCAPI") -> typing.Any:
        pass

    @abstractmethod
    def construct(
            self,
            views: typing.Dict[str, "ABCView"],
            state_dispenser: ABCStateDispenser,
            error_handler: ABCErrorHandler,
    ) -> "ABCRouter":
        pass

    def add_view(self, name: str, view: "ABCView") -> typing.NoReturn:
        self.views[name] = view

    def view(self, name: str) -> typing.Callable[..., typing.Type["ABCView"]]:
        def decorator(view: typing.Type["ABCView"]):
            self.add_view(name, view())
            return view

        return decorator
