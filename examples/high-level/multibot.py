from tottle import Bot, Message, run_multibot
from tottle.api import API

bot = Bot()


@bot.on.message(lev="multibot?")
async def multibot_example(message: Message):
    await message.answer("Yes! I'm running on multiple tokens!")


run_multibot(bot, apis=(API("First token"), API("Second token")))  # There can be as many tokens as you want
