import os
import asyncio

from tottle import Bot

bot = Bot(os.environ["TELEGRAM_TOKEN"])


async def start_listening():
    """
    Implement your low-level logic here.
    No additional tools. Only raw events.
    """
    async for event in bot.polling.listen():  # type: ignore
        ...


asyncio.run(start_listening())
