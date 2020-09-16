import os

from tottle import Bot, Message
from tottle.dispatch.rules import TextRule
from tottle.types.responses.keyboard import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardRemove
)

bot = Bot(os.environ["TELEGRAM_TOKEN"])
keyboard = ReplyKeyboardMarkup().add_buttons(
    KeyboardButton(text="How are you?")
)


@bot.on.message(TextRule("hello", ignore_case=True))
async def _(message: Message):
    """
    Answers "Hi!" to any message containing
    "hello" and then sends the keyboard
    """
    await message.answer("Hi!", reply_markup=keyboard.dict())


@bot.on.message(TextRule("How are you?"))
async def _(message: Message):
    """
    Answers to message and then removes
    the reply keyboard
    """
    await message.answer(
        "I'm good. Thanks for asking!",
        reply_markup=ReplyKeyboardRemove().dict()
    )

bot.run_polling()
