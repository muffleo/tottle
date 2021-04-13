<p align="center">
  <a href="https://github.com/tottle-project/tottle-python">
    <img src="/logo.jpg" width="250px" style="display: inline-block;">
  </a>
</p>
 
<h1 align="center">Tottle — fast, flexible and flawless Telegram API wrapper</h1>
   
## How to install
At the moment `tottle` is only available for download directly from GitHub:

`pip install -U https://github.com/tottle-project/tottle-python/archive/master.zip`

## Getting started
### Longpoll
This is the fastest way to launch a bot. Here is an example:
```python
from tottle import Bot, Message

bot = Bot("token-here")

@bot.on.message()
async def message_handler(_) -> str:
    return "Hello world!"

bot.run_forever()
```
In this example, the bot replies to all messages in any chat. You can also specify a pattern for text match (or even give it a [vbml](https://github.com/tesseradecade/vbml) pattern). For more examples visit [examples](./examples) directory.
### Callback
The example is not ready yet, but you can actually implement handling of Callback API updates via `bot.router.route(event: dict, api: API)` method. The implementation depends on the web framework you are using.

## Using
 - Heavily based on [vkbottle](https://github.com/timoniq/vkbottle)
 - Powered by [aiohttp](https://github.com/aio-libs/aiohttp)
 - Response models built with [pydantic](https://github.com/samuelcolvin/pydantic)
 - Text validation is implemented through [vbml](https://github.com/tesseradecade/vbml)

## Contributing
Because the whole library is not actually completed, we are always glad to see your support. This is a list of our current goals:

| Plan to add           | In progress                | Completed                  |
|-----------------------|----------------------------|----------------------------|
|                       | API and its object types   | Middlewares                |
|                       | Generating (keyboard etc.) | Polling                    |
|                       |                            | HTTP Client                |
|                       |                            | State dispenser            |
|                       |                            | Return Manager             |
|                       |                            | Blueprints                 |
|                       |                            | Exception factory          |
