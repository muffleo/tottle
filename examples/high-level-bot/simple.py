import os

from tottle import Bot, Message
from tottle.dispatch.rules import VBMLRule

bot = Bot(os.environ["TELEGRAM_TOKEN"])


@bot.on.private_message(VBMLRule(["hi", "hello"], ignore_case=True))
async def greet_handler(message: Message):
    """
    Reacts to all messages containing
    "hi" or "hello" and ignores text case
    """
    await bot.api.messages.send_message(
        text="Hi!", chat_id=message.chat.id,
    )


bot.run_polling()
