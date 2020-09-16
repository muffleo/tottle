import os

from tottle import Bot, Message
from tottle.dispatch.rules import TextRule

bot = Bot(os.environ["TELEGRAM_TOKEN"])


@bot.on.private_message(TextRule(["hi", "hello"], ignore_case=True))
async def _(message: Message):
    """
    Reacts to all messages containing
    "hi" or "hello" and ignores text case
    """
    await message.answer("Hi!")


bot.run_polling()
