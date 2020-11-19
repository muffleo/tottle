from tottle.types.minis.message import MessageMini as Message
from tottle.types.state import BaseStateGroup
from tottle.dispatch.rules import ABCRule
from tottle.tools.enums import ChatType

import re
import vbml
import typing
from abc import abstractmethod
from typing import Union, List, Optional

DEFAULT_PREFIXES = ["!", "/"]


class ABCMessageRule(ABCRule):
    @abstractmethod
    async def check(self, message: Message) -> bool:
        pass


class PeerRule(ABCMessageRule):
    def __init__(self, from_chat: bool = True):
        self.from_chat = from_chat

    async def check(self, message: Message) -> Union[dict, bool]:
        if message.chat.id != message.sender.id:
            return self.from_chat
        return not self.from_chat


class CommandRule(ABCMessageRule):
    def __init__(self, text: str, prefixes: Optional[List[str]] = None):
        self.prefixes = prefixes or []
        self.text = text

    async def check(self, message: Message) -> bool:
        for prefix in self.prefixes:
            if message.text == prefix + self.text:
                return True
            return False


class LevensteinRule(ABCMessageRule):
    def __init__(self, levenstein_texts: Union[List[str], str], max_distance: int = 1):
        if isinstance(levenstein_texts, str):
            levenstein_texts = [levenstein_texts]
        self.levenstein_texts = levenstein_texts
        self.max_distance = max_distance

    @staticmethod
    def distance(a: str, b: str) -> int:
        n, m = len(a), len(b)
        if n > m:
            a, b = b, a
            n, m = m, n

        current_row = range(n + 1)
        for i in range(1, m + 1):
            previous_row, current_row = current_row, [i] + [0] * n  # type: ignore
            for j in range(1, n + 1):
                add, delete, change = (
                    previous_row[j] + 1,
                    current_row[j - 1] + 1,
                    previous_row[j - 1],
                )
                if a[j - 1] != b[i - 1]:
                    change += 1
                current_row[j] = min(add, delete, change)  # type: ignore

        return current_row[n]

    async def check(self, message: Message) -> Union[dict, bool]:
        for levenstein_text in self.levenstein_texts:
            if self.distance(message.text, levenstein_text) <= self.max_distance:
                return True
        return False


class MatchRule(ABCMessageRule):
    def __init__(
        self,
        pattern: Union[str, "vbml.Pattern", List[Union[str, "vbml.Pattern"]]],
        patcher: Optional["vbml.Patcher"] = None,
        flags: Optional[re.RegexFlag] = None,
    ):
        flags = flags or self.config.get("vbml_flags")

        if isinstance(pattern, str):
            pattern = [vbml.Pattern(pattern, flags=flags or self.config.get("vbml_flags"))]
        elif isinstance(pattern, vbml.Pattern):
            pattern = [pattern]
        elif isinstance(pattern, list):
            pattern = [p if isinstance(p, vbml.Pattern) else vbml.Pattern(p) for p in pattern]

        self.patterns = pattern
        self.patcher = patcher or self.config["vbml_patcher"]

    async def check(self, message: Message) -> Union[dict, bool]:
        for pattern in self.patterns:
            result = self.patcher.check(pattern, message.text)
            if result not in (None, False):
                return result
        return False


class RegexRule(ABCMessageRule):
    def __init__(self, regexp: Union[str, List[str], typing.Pattern, List[typing.Pattern]]):
        if isinstance(regexp, typing.Pattern):
            regexp = [regexp]
        elif isinstance(regexp, str):
            regexp = [re.compile(regexp)]
        elif isinstance(regexp, list):
            regexp = [re.compile(exp) for exp in regexp]

        self.regexp = regexp

    async def check(self, message: Message) -> Union[dict, bool]:
        for regexp in self.regexp:
            match = re.match(regexp, message.text)
            if match:
                return {"match": match.groups()}
        return False


class StateRule(ABCMessageRule):
    def __init__(self, state: Union[List[BaseStateGroup], BaseStateGroup]):
        if not isinstance(state, list):
            state = [state]
        self.state = state

    async def check(self, message: Message) -> bool:
        if message.state_peer is None:
            return bool(self.state)
        return message.state_peer.state in self.state
