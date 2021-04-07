import asyncio
import json
import typing

from aiohttp import ClientSession, TCPConnector

from .abc import ABCHTTPClient


class AiohttpClient(ABCHTTPClient):
    def __init__(
            self,
            loop: typing.Optional[asyncio.AbstractEventLoop] = None,
            session: typing.Optional[ClientSession] = None,
            *args,
            **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.loop = loop or asyncio.get_event_loop()
        self.session = session or ClientSession(
            connector=TCPConnector(ssl=False),
            json_serialize=json.dumps,
        )

    async def request_json(
            self, method: str, url: str, data: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        async with self.session.request(method, url, data=data, **kwargs) as response:
            return await response.json(loads=json.loads)

    async def request_text(
            self, method: str, url: str, data: typing.Optional[dict] = None, **kwargs
    ) -> str:
        async with self.session.request(method, url, data=data, **kwargs) as response:
            return await response.text()

    async def request_content(
            self, method: str, url: str, data: typing.Optional[dict] = None, **kwargs
    ) -> bytes:
        async with self.session.request(method, url, data=data, **kwargs) as response:
            return await response.content.read()

    async def close(self) -> typing.NoReturn:
        await self.session.close()
