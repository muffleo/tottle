from tottle.dispatch.rules import ABCRule
from tottle.dispatch.views import ABCView
from tottle.types.responses.chat import Message

from abc import ABC, abstractmethod
from typing import Callable, Any, Dict

LabeledMessageHandler = Callable[..., Callable[[Message], Any]]


class ABCBotLabeler(ABC):
    @abstractmethod
    def message(self, *rules: "ABCRule", **custom_rules) -> LabeledMessageHandler:
        pass

    @abstractmethod
    def chat_message(self, *rules: "ABCRule", **custom_rules) -> LabeledMessageHandler:
        pass

    @abstractmethod
    def private_message(
        self, *rules: "ABCRule", **custom_rules
    ) -> LabeledMessageHandler:
        pass

    @abstractmethod
    def views(self) -> Dict[str, "ABCView"]:
        pass

    @abstractmethod
    def load(self, labeler: Any):
        pass
