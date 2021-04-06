<p align="center">
     <a href="https://vk.me/join/AJQ1d3monBhyfSe2JBjXNoyb">
         <img src="https://img.shields.io/badge/-VK%20Chat-blue" alt="VK Chat — join us!">
     </a>
 </p>
<h1 align="center">Tottle — fast, async & powerful Telegram API wrapper</h1>
<p align="center">This project no longer receives active support due to lack of time and effort. We are currently looking for a maintainer who can continue to work on it. That being said, any support such as pull requests is welcome, so feel free to contribute!</p>
   
## Examples
### "Hello, World!" example
In this example, the bot reacts to any message and sends reply.
```python
from tottle import Bot, Message

bot = Bot("token-here")

@bot.on.private_message()
async def greet_handler(message: Message):
    await message.reply("Hello, world!")

bot.run_forever()
```
Also, you can specify a pattern for text match (or even give it a [vbml](https://github.com/tesseradecade/vbml) pattern). For more examples visit [examples](./examples) directory.

## Using
 - Based on [vkbottle](https://github.com/timoniq/vkbottle)
 - Powered by [aiohttp](https://github.com/aio-libs/aiohttp)
 - Response models built with [pydantic](https://github.com/samuelcolvin/pydantic)
 - Text validation is implemented through [vbml](https://github.com/tesseradecade/vbml)

## Contributing
Because the whole library is not actually completed, we are always glad to see your support. This is a list of our current goals:

| Plan to add           | In progress                | Completed                  |
|-----------------------|----------------------------|----------------------------|
| Proper error handling | API and its object types   | Middlewares                |
| Return Manager        | Generating (keyboard etc.) | Polling                    |
| Blueprints            | State dispenser            | HTTP Client                |
