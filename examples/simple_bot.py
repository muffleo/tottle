import os

from tottle import Bot, Message

bot = Bot(os.environ["TELEGRAM_TOKEN"])


@bot.on.message(text="hi<!>")
async def _(message: Message):
    """
    Reacts to all messages containing
    "hi" or anything else
    :param message:
    :return:
    """
    await bot.api.bot.send_message(
        text="Hi!", chat_id=message.chat.id
    )


bot.run_polling()
