import asyncio
import os

from tottle import API

api = API(os.environ["TELEGRAM_TOKEN"])


async def main():
    user = await api.users.get_me()  # Make request to Telegram API..
    print(user)  # ..and print the response


asyncio.get_event_loop().run_until_complete(main())
