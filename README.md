<p align="center">
  <a href="https://github.com/tottle-project/tottle-python">
    <img src="/logo.jpg" width="250px" style="display: inline-block;">
  </a>
</p>
 
<h1 align="center">Tottle — fast, flexible and flawless Telegram API wrapper</h1>

## How to install
1) Installing the stable version of tottle is as easy as:
    ```shell script
    pip install -U tottle
    ```

2) If you want to install the latest version, you can do:
    ```shell script
   pip install -U https://github.com/tottle-project/tottle-python/archive/master.zip
   ```

## Getting started

### Longpoll

This is the fastest way to launch bot. Here is the example:

```python
from tottle import Bot

bot = Bot("token")

@bot.on.message()
async def message_handler(_) -> str:
    return "Hello world!"

bot.run_forever()
```

In this example, bot replies to all messages in any chat. You can also specify a pattern for text matching (or even give it a [vbml](https://github.com/tesseradecade/vbml) pattern). For more examples visit [examples](./examples) directory.

### Callback

This example is not ready yet, but you can actually implement handling of Callback API updates via `bot.router.route(event: dict, api: API)` method. The implementation depends on what web framework you use.

## Using
 - Inspired and based (all architectural signatures) on [vkbottle](https://github.com/timoniq/vkbottle)
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
