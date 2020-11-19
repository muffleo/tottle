import os

from tottle import Bot, Message
from tottle.types.responses.keyboard import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardRemove,
)

bot = Bot(os.environ["TELEGRAM_TOKEN"])
bot.labeler.vbml_ignore_case = True

keyboard = ReplyKeyboardMarkup().add_buttons(
    KeyboardButton(text="How are you?")
)
remove_keyboard = ReplyKeyboardRemove()


@bot.on.message(text="hello")
async def greet_handler(message: Message):
    await message.answer("Hi!", reply_markup=keyboard.dict())


@bot.on.message(text="how are you")
async def question_handler(message: Message):
    await message.answer("I'm good. Thanks for asking!", reply_markup=remove_keyboard.dict())

bot.run_forever()
