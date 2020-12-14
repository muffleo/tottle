from tottle import Bot, Message, run_multibot
from tottle.api import API

bot = Bot(token="TELEGRAM_TOKEN")


@bot.on.message(lev="multibot?")
async def multibot_example(message: Message):
    await message.answer("Yes! I'm running on multiple tokens!")


run_multibot(bot, apis=(API("first token"), API("second token")))  # There can be as many tokens as you want
