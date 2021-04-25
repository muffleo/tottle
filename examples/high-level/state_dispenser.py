from tottle.types import BaseStateGroup
from tottle import Bot, Message

bot = Bot(token="Your token")


class ProfileState(BaseStateGroup):
    NAME = 0
    AGE = 1


# <state=None> (default) handles all events with no state;
# <state="*"> handles all events with and without state
# you can add StateRule to auto_rules in blueprint for example
@bot.on.message(text="Hello", state=None)
async def greeting(message: Message):
    await message.answer(
        "Good to see you!\n"
        "What's your name?"
    )
    # To transfer data to other functions via state, you can use kwargs
    await bot.state_dispenser.set(message.sender.id, ProfileState.NAME)


@bot.on.message(state=ProfileState.NAME)
async def greeting_name(message: Message):
    await message.answer(
        "You're name is beautiful!\n"
        "Please write your age"
    )
    await bot.state_dispenser.set(message.sender.id, ProfileState.AGE)


@bot.on.message(state=ProfileState.AGE)
async def greeting_age(message: Message):
    await message.answer(
        "Nice to meet you!\n"
        "Write to me whenever you want to talk!"
    )
    await bot.state_dispenser.delete(message.sender.id)


bot.run_forever()
