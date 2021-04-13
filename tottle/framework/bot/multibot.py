from typing import Iterable, Type
from loguru import logger

from tottle.api import ABCAPI
from tottle.http import SingleSessionManager, AiohttpClient
from tottle.polling import ABCPolling, BotPolling
from .bot import Bot


def run_multibot(
    bot: Bot, apis: Iterable[ABCAPI], polling_type: Type[ABCPolling] = BotPolling
):
    """Add run_polling with polling constructed from derived apis
    :param bot: Bot main instance (api is not required)
    :param apis: Iterable of apis
    :param polling_type: polling type to be ran
    """
    for i, api_instance in enumerate(apis):
        logger.debug(f"Connecting API (index: {i})")
        polling = polling_type().construct(api_instance)
        api_instance.http = SingleSessionManager(AiohttpClient)
        bot.apis = apis
        bot.loop_wrapper.add_task(bot.run_polling(custom_polling=polling, apis_count=i))

    bot.loop_wrapper.run_forever(bot.loop)
