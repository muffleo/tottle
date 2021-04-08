from tottle import Bot

from blueprints import bps


bot = Bot(token="Your token")


# To work correctly, you need to run blueprints
for bp in bps:
    bp.load(bot)


bot.run_forever()
