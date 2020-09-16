import json

from asyncio import AbstractEventLoop, get_event_loop
from typing import Optional

from tottle.http import AiohttpClient
from tottle.const import __version__, VERSION_SOURCE
from tottle.utils.logger import logger


class Updater:
    def __init__(
            self,
            loop: Optional[AbstractEventLoop] = None,
    ):
        self.loop = loop or get_event_loop()
        self.http: AiohttpClient = AiohttpClient(loop)

    def check_version(self):
        source = self.loop.run_until_complete(
            self.http.request_text(
                "GET", VERSION_SOURCE
            )
        )

        try:
            source = json.loads(source)
        except json.JSONDecodeError:
            logger.warning("Unable to check version")

        if source.get("version") != __version__:
            logger.warning(
                "Old version! Update was found: v. {} | {}",
                source.get("version"), source.get("description")
            )

        self.loop.run_until_complete(self.http.close())
