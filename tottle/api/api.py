import typing

from tottle.api.abc import ABCAPI
from tottle.http import (
    ABCSessionManager,
    SingleSessionManager,
    AiohttpClient
)
from tottle.types.categories import APICategories
from tottle.tools.exceptions import TelegramError


class API(ABCAPI, APICategories):
    API_URL = "https://api.telegram.org/"

    def __init__(
            self,
            token: str,
            session_manager: typing.Optional[SingleSessionManager] = None,
    ) -> None:
        self.token: str = token
        self.request_url: str = self.API_URL + f"bot{self.token}/"
        self.http: ABCSessionManager = session_manager or SingleSessionManager(AiohttpClient)

    async def request(
            self,
            method: str,
            data: typing.Optional[dict] = None,
    ) -> typing.Optional[typing.Any]:

        async with self.http as session:
            response = await session.request_json(
                "POST", url=self.request_url + method,
                json=data or {},
            )

            if not response.get("ok"):
                raise TelegramError(
                    "Request to API with method {} and params {} failed: "
                    "{description} ({error_code})".format(
                        method, data, **response
                    )
                )

            return response.get("result")

    @property
    def instance(self) -> "API":
        return self
