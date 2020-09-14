import os

from tottle import Bot, Message
from tottle.polling.rules import TextRule

bot = Bot(os.environ["TELEGRAM_TOKEN"])


@bot.on.message(TextRule(["hi", "hello"], ignore_case=True))
async def _(message: Message):
    """
    Reacts to all messages containing
    "hi" or "hello" and ignores text case
    :param message:
    :return:
    """
    await bot.api.messages.send_message(
        text="Hi!", chat_id=message.chat.id,
    )


bot.run_polling()
