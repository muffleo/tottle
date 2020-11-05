import os

from tottle import Bot, Message
from tottle.dispatch.rules import MatchRule
from tottle.types.responses.keyboard import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardRemove
)

bot = Bot(os.environ["TELEGRAM_TOKEN"])
keyboard = ReplyKeyboardMarkup().add_buttons(
    KeyboardButton(text="How are you?")
)
remove_keyboard = ReplyKeyboardRemove()


@bot.on.message(MatchRule("hello", ignore_case=True))
async def greet_handler(message: Message):
    await message.answer("Hi!", reply_markup=keyboard.dict())


@bot.on.message(MatchRule("how are you?", ignore_case=True))
async def question_handler(message: Message):
    await message.answer(
        "I'm good. Thanks for asking!",
        reply_markup=remove_keyboard.dict()
    )

bot.run_polling()
