import os
import asyncio

from tottle import Bot
from tottle.utils.logger import logger

bot = Bot(os.environ["TELEGRAM_TOKEN"])


async def start_listening():
    async for event in bot.polling.listen():
        # Implement your low-level logic here
        logger.info(event)

asyncio.run(start_listening())
