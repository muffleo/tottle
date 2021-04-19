import os

from tottle import Bot, Message

bot = Bot(os.environ["TELEGRAM_TOKEN"])
bot.labeler.vbml_ignore_case = True


@bot.on.private_message(text="my name is <name>")
async def prompt_handler(message: Message, name: str):
    await message.answer(f"Hello, {name}!")


bot.run_forever()
