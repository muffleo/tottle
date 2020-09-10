from abc import abstractmethod
from typing import Union, List

import vbml

from tottle.polling.rules import ABCRule
from tottle.types.responses.update import Update


class ABCMessageRule(ABCRule):
    @abstractmethod
    async def check(self, event: Update) -> bool:
        pass


class VBMLRule(ABCMessageRule):
    def __init__(
            self,
            pattern: Union[str, "vbml.Pattern", List[Union[str, "vbml.Pattern"]]],
            patcher: "vbml.Patcher",
    ):
        if isinstance(pattern, str):
            pattern = [vbml.Pattern(pattern)]
        elif isinstance(pattern, vbml.Pattern):
            pattern = [pattern]
        elif isinstance(pattern, list):
            pattern = [p if isinstance(p, vbml.Pattern) else vbml.Pattern(p) for p in pattern]
        self.patterns = pattern
        self.patcher = patcher

    async def check(self, event: Update) -> Union[dict, bool]:
        for pattern in self.patterns:
            result = self.patcher.check(
                pattern, event.message.text
            )

            if isinstance(result, dict):
                return result
        return False
