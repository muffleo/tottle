from typing import Union, Any, Callable

from .abc import ABCHandler
from ..rules import ABCRule


class FunctionHandler(ABCHandler):
    def __init__(self, handler: Callable, *rules: "ABCRule", blocking: bool = True):
        self.handler = handler
        self.rules = rules
        self.blocking = blocking

    async def filter(self, event: Any) -> Union[dict, bool]:
        rule_context = {}

        for rule in self.rules:
            result = await rule.check(event)

            if result is False:
                return False
            elif isinstance(result, dict):
                rule_context.update(result)

        return rule_context

    async def process(self, event: Any, **context) -> Any:
        return await self.handler(event, **context)

    def __repr__(self):
        return f"<FromFuncHandler {self.handler.__name__} blocking={self.blocking} rules={self.rules}>"
