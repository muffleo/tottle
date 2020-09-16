import typing

from tottle.api import API
from tottle.dispatch.routers import BotRouter


class Polling:
    def __init__(self, api: "API", router: "BotRouter"):
        self.api = api
        self.router = router

        self.offset: int = 0
        self.stop: bool = False

    async def get_raw_updates(self) -> typing.Optional[typing.List[dict]]:
        raw_updates = await self.api.request(
            "getUpdates", {"offset": self.offset}
        )

        return raw_updates

    async def listen(self) -> typing.AsyncIterator[dict]:
        while not self.stop:
            updates = await self.get_raw_updates()

            for update in updates:
                self.offset = updates[-1]["update_id"] + 1
                yield update

    async def run(self) -> typing.NoReturn:
        async for update in self.listen():
            await self.router.route(update, self.api)
