import os

from tottle import Bot, Message
from tottle.dispatch.rules import MatchRule

bot = Bot(os.environ["TELEGRAM_TOKEN"])


@bot.on.private_message(MatchRule("my name is <name>", ignore_case=True))
async def prompt_handler(message: Message, name: str):
    await message.answer(f"Hello, {name}!")


bot.run_polling()
