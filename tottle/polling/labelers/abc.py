from abc import ABC, abstractmethod
from typing import Callable, Any, Dict, Optional, Type, List

from vbml import Patcher

from tottle.types.responses.chat import Message
from ..rules import ABCRule, VBMLRule

LabeledMessageHandler = Callable[..., Callable[[Message], Any]]


class ABCBotLabeler(ABC):
    def __init__(
            self,
            custom_rules: Optional[Dict[str, Type["ABCRule"]]] = None,
            patcher: Optional[Patcher] = None,
    ):
        self.patcher = patcher or Patcher()
        self.custom_rules = custom_rules or {}
        self.custom_rules["text"] = self.get_vbml_rule  # type: ignore

    @abstractmethod
    def message(self, *rules: "ABCRule", **custom_rules) -> LabeledMessageHandler:
        pass

    def get_custom_rules(self, custom_rules: Dict[str, Any]) -> List["ABCRule"]:
        return [self.custom_rules[k](v) for k, v in custom_rules.items()]  # type: ignore

    def get_vbml_rule(self, pattern: Any) -> "VBMLRule":
        return VBMLRule(pattern, self.patcher)
