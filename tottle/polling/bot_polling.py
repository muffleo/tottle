from typing import Optional, AsyncIterator, List

from tottle.api import ABCAPI
from tottle.polling import ABCPolling
from tottle.exception_factory import ABCErrorHandler, ErrorHandler


class BotPolling(ABCPolling):
    def __init__(
            self,
            api: Optional[ABCAPI] = None,
            offset: Optional[int] = None,
            error_handler: Optional[ABCErrorHandler] = None,
    ):
        self._api = api
        self.error_handler = error_handler or ErrorHandler()
        self.offset: int = offset or 0
        self.stop: bool = False

    async def get_updates(self) -> Optional[List[dict]]:
        raw_updates = await self.api.request(
            "getUpdates", {
                "offset": self.offset
            }
        )

        return raw_updates

    async def listen(self) -> AsyncIterator[dict]:
        while not self.stop:

            try:
                updates = await self.get_updates()

                for update in updates:
                    self.offset = updates[-1]["update_id"] + 1
                    yield update
            except BaseException as e:
                await self.error_handler.handle(e)

    def construct(
            self,
            api: "ABCAPI",
            error_handler: Optional["ABCErrorHandler"] = None
    ) -> "BotPolling":
        self._api = api

        if error_handler is not None:
            self.error_handler = error_handler

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
