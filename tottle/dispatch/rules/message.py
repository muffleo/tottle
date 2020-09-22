import re
from abc import abstractmethod
from typing import Union, List

import vbml

from tottle.types.responses.chat import Message
from tottle.dispatch.rules import ABCRule
from tottle.utils.enums import ChatType

patcher = vbml.Patcher()


class ABCMessageRule(ABCRule):
    @abstractmethod
    async def check(self, message: Message) -> bool:
        pass


class FromChatRule(ABCMessageRule):
    async def check(self, message: Message) -> bool:
        return message.chat.type in (ChatType.GROUP, ChatType.SUPERGROUP)


class PrivateMessageRule(ABCMessageRule):
    async def check(self, message: Message) -> bool:
        return message.chat.type == ChatType.PRIVATE


class VBMLRule(ABCMessageRule):
    def __init__(
            self,
            pattern: Union[
                str, "vbml.Pattern", List[
                    Union[str, "vbml.Pattern"],
                ]
            ],
            ignore_case: bool = False,
    ):
        if isinstance(pattern, str):
            pattern = [vbml.Pattern(pattern, flags=re.IGNORECASE if ignore_case else None)]
        elif isinstance(pattern, vbml.Pattern):
            pattern = [pattern]
        elif isinstance(pattern, list):
            pattern = [
                p if isinstance(p, vbml.Pattern)
                else vbml.Pattern(p, flags=re.IGNORECASE if ignore_case else None)
                for p in pattern
            ]
        self.patterns = pattern

    async def check(self, message: Message) -> Union[dict, bool]:
        for pattern in self.patterns:
            result = patcher.check(
                pattern, message.text
            )

            if result not in (None, False):
                return result
        return False
