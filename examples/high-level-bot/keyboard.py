from tottle import Bot, Message
from tottle.tools import Keyboard, Button, InlineKeyboard, InlineButton


bot = Bot(token="Your token")

# Creating keyboard objects
keyboard = (
    Keyboard(resize_keyboard=True)
    .add(Button(text="Hello!"))
    .row()
    .add(Button(text="Bye!"))
)
inline_keyboard = (
    InlineKeyboard()
    .add(InlineButton(text="Tottle", url="https://github.com/tottle-project/tottle-python"))
)


@bot.on.message(text="Keyboard")
async def answer(message: Message):
    # Using the reply_markup parameter, we specify the keyboard object
    await message.answer("Hold the keyboard!", reply_markup=keyboard.dict())


@bot.on.message(text="Inline keyboard")
async def answer(message: Message):
    await message.answer("Hold the inline keyboard!", reply_markup=inline_keyboard.dict())


bot.run_forever()
