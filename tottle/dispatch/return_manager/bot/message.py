from typing import TYPE_CHECKING, Union

from tottle.dispatch.return_manager import BaseReturnManager

if TYPE_CHECKING:
    from tottle.types.minis.message import MessageMini


class BotMessageReturnHandler(BaseReturnManager):
    @BaseReturnManager.instance_of(str)
    async def str_handler(self, value: str, message: "MessageMini", _: dict):
        await message.answer(value)

    @BaseReturnManager.instance_of((tuple, list))
    async def iter_handler(self, value: Union[tuple, list], message: "MessageMini", _: dict):
        [await message.answer(str(e)) for e in value]

    @BaseReturnManager.instance_of(dict)
    async def dict_handler(self, value: dict, message: "MessageMini", _: dict):
        await message.answer(**value)
