import os

from tottle import Bot, Message
from tottle.dispatch.middlewares import BaseMiddleware

bot = Bot(os.environ["TELEGRAM_TOKEN"])


class Middleware(BaseMiddleware):
    async def pre(self, event: Message):
        await event.answer("Middleware worked!")


@bot.on.private_message(text="/start")
async def message_handler(message: Message):
    await message.answer("Hello! I am bot.")


bot.labeler.message_view.register_middleware(Middleware())
bot.run_forever()
