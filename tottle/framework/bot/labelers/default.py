from tottle.framework.bot.labelers import ABCBotLabeler, LabeledMessageHandler
from tottle.dispatch.handlers import FunctionHandler
from tottle.dispatch.rules import ABCRule
from tottle.dispatch.rules.bot import (
    PeerRule,
    MatchRule,
    StateRule,
    RegexRule,
    LevensteinRule,
    MessageLengthRule,
    CommandRule,
)
from tottle.dispatch.views import ABCView, MessageView

import re
import vbml
from typing import Dict, Type, Any, List

DEFAULT_CUSTOM_RULES: Dict[str, Type[ABCRule]] = {
    "text": MatchRule,
    "command": CommandRule,
    "regex": RegexRule,
    "state": StateRule,
    "levenstein": LevensteinRule,
    "lev": LevensteinRule,
    "from_chat": PeerRule,
    "length": MessageLengthRule,
}


class BotLabeler(ABCBotLabeler):
    def __init__(self, **kwargs):
        self.message_view = MessageView()

        self.custom_rules = kwargs.get("custom_rules") or DEFAULT_CUSTOM_RULES
        self.rule_config: Dict[str, Any] = {
            "vbml_flags": re.MULTILINE,
            "vbml_patcher": vbml.Patcher(),
        }

    @property
    def vbml_ignore_case(self) -> bool:
        """ Gets ignore case flag from rule config flags """
        return re.IGNORECASE in self.rule_config["flags"]

    @vbml_ignore_case.setter
    def vbml_ignore_case(self, ignore_case: bool):
        """Adds ignore case flag to rule config flags or removes it"""
        if not ignore_case:
            self.rule_config["vbml_flags"] ^= re.IGNORECASE
        else:
            self.rule_config["vbml_flags"] |= re.IGNORECASE

    @property
    def vbml_patcher(self) -> vbml.Patcher:
        return self.rule_config["vbml_patcher"]

    @vbml_patcher.setter
    def vbml_patcher(self, patcher: vbml.Patcher):
        self.rule_config["vbml_patcher"] = patcher

    @property
    def vbml_flags(self) -> re.RegexFlag:
        return self.rule_config["vbml_flags"]

    @vbml_flags.setter
    def vbml_flags(self, flags: re.RegexFlag):
        self.rule_config["vbml_flags"] = flags

    def message(self, *rules: "ABCRule", **custom_rules) -> LabeledMessageHandler:
        def decorator(func):
            self.message_view.handlers.append(
                FunctionHandler(
                    func,
                    *rules,
                    *self.get_custom_rules(custom_rules),
                )
            )
            return func

        return decorator

    def chat_message(self, *rules: "ABCRule", **custom_rules) -> LabeledMessageHandler:
        def decorator(func):
            self.message_view.handlers.append(
                FunctionHandler(
                    func,
                    PeerRule(True),
                    *rules,
                    *self.get_custom_rules(custom_rules),
                )
            )
            return func

        return decorator

    def private_message(
        self, *rules: "ABCRule", **custom_rules
    ) -> LabeledMessageHandler:
        def decorator(func):
            self.message_view.handlers.append(
                FunctionHandler(
                    func,
                    PeerRule(False),
                    *rules,
                    *self.get_custom_rules(custom_rules),
                )
            )
            return func

        return decorator

    def load(self, labeler: "BotLabeler"):
        self.message_view.handlers.extend(labeler.message_view.handlers)
        self.message_view.middlewares.extend(labeler.message_view.middlewares)

    def get_custom_rules(self, custom_rules: Dict[str, Any]) -> List["ABCRule"]:
        return [self.custom_rules[k].with_config(self.rule_config)(v) for k, v in custom_rules.items()]  # type: ignore

    def views(self) -> Dict[str, "ABCView"]:
        return {"message": self.message_view}
