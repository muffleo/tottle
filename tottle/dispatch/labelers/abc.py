from abc import ABC, abstractmethod
from typing import Callable, Any, Dict, Optional, Type, List

from vbml import Patcher
from ..rules import ABCRule
from ...types.mini import MessageMini

LabeledMessageHandler = Callable[..., Callable[[MessageMini], Any]]


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

    def get_custom_rules(self, custom_rules: Dict[str, Any]) -> List["ABCRule"]:
        return [self.custom_rules[k](v) for k, v in custom_rules.items()]  # type: ignore
