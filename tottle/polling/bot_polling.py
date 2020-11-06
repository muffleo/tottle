import typing

from tottle.api import ABCAPI
from tottle.polling import ABCPolling


class BotPolling(ABCPolling):
    def __init__(
            self,
            api: typing.Optional[ABCAPI] = None,
            offset: typing.Optional[int] = None,
    ):
        self._api = api
        self.offset: int = offset or 0
        self.stop: bool = False

    async def get_updates(self) -> typing.Optional[typing.List[dict]]:
        raw_updates = await self.api.request(
            "getUpdates", {
                "offset": self.offset
            }
        )

        return raw_updates

    async def listen(self) -> typing.AsyncIterator[dict]:
        while not self.stop:
            updates = await self.get_updates()

            for update in updates:
                self.offset = updates[-1]["update_id"] + 1
                yield update

    def construct(self, api: "ABCAPI") -> "BotPolling":
        self._api = api
        return self

    @property
    def api(self) -> "ABCAPI":
        if self._api is None:
            raise NotImplementedError(
                "You must construct polling with API "
                "before try to access api property of Polling"
            )
        return self._api

    @api.setter
    def api(self, new_api: "ABCAPI"):
        self._api = new_api
