from tottle.dispatch.rules import ABCRule
from tottle.dispatch.views import ABCView
from tottle.types.responses.chat import Message

from abc import ABC, abstractmethod
from typing import Callable, Any, Dict, Optional, Type, List
from vbml import Patcher

LabeledMessageHandler = Callable[..., Callable[[Message], Any]]


class ABCBotLabeler(ABC):
    def __init__(
            self,
            custom_rules: Optional[Dict[str, Type["ABCRule"]]] = None,
            patcher: Optional[Patcher] = None,
    ):
        self.patcher = patcher or Patcher()
        self.custom_rules = custom_rules or {}

    @abstractmethod
    def message(
            self, *rules: "ABCRule", **custom_rules
    ) -> LabeledMessageHandler:
        pass

    @abstractmethod
    def chat_message(
            self, *rules: "ABCRule", **custom_rules
    ) -> LabeledMessageHandler:
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

    def get_custom_rules(self, custom_rules: Dict[str, Any]) -> List["ABCRule"]:
        return [self.custom_rules[k](v) for k, v in custom_rules.items()]  # type: ignore
