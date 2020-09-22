import os

from tottle import Bot, Message
from tottle.dispatch.rules import VBMLRule
from tottle.types.responses.keyboard import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardRemove
)

bot = Bot(os.environ["TELEGRAM_TOKEN"])
keyboard = ReplyKeyboardMarkup().add_buttons(
    KeyboardButton(text="How are you?")
)


@bot.on.message(VBMLRule("hello", ignore_case=True))
async def _(message: Message):
    """
    Answers "Hi!" to any message containing
    "hello" and then sends the keyboard
    """
    await bot.api.messages.send_message(
        text="Hi!", chat_id=message.chat.id,
        reply_markup=keyboard.dict()
    )


@bot.on.message(VBMLRule("How are you?"))
async def _(message: Message):
    """
    Answers to message and then removes
    the reply keyboard
    """
    await bot.api.messages.send_message(
        text="I'm good. Thanks for asking!",
        chat_id=message.chat.id,
        reply_markup=ReplyKeyboardRemove().dict()
    )

bot.run_polling()
