import os
import asyncio

from tottle import API

api = API(os.environ["TELEGRAM_TOKEN"])


async def main():
    user = await api.users.get_me()  # Make request to Telegram API..
    print(user)  # ..and print the response


asyncio.run(main())
