# Tottle — really handy Telegram API wrapper
<a href="https://vk.me/join/AJQ1d3monBgV17SC1lRCtz1j">
    <img src="https://img.shields.io/badge/VK%20Chat-join-blue" alt="VK Chat — join us!">
</a>
<a href="https://t.me/joinchat/S_jqPhhhWD9iDODdMeQx3Q">
    <img src="https://img.shields.io/badge/Telegram%20Chat-join-informational" alt="Telegram Chat — join us!">
</a>

---------------------------------------

## About
Tottle is a _fast_, _convenient_ and _extensible_ library for working with the Telegram Bot API. **Still in development.**
### Plan to add
- FSM
- Generating (keyboard etc.)
- Callback updates listening method
### In progress/completed
- Polling
- HTTP client
- API and its object types (almost completed)

## Examples
### Longpoll
In this example bot reacts to all messages containing "hi" or anything else. Thanks to [vbml](https://github.com/tesseradecade/vbml), it is really easy:
```python
from tottle import Bot, Message

bot = Bot("token-here")

@bot.on.message(text="hi")
async def message_handler(message: Message):
    await bot.api.bot.send_message(
        text="Hi!", chat_id=message.chat.id
    )
```
You can find more examples in the [examples](./examples) directory.

## Using
 - Based on [vkbottle](https://github.com/timoniq/vkbottle)
 - Powered by [aiohttp](https://github.com/aio-libs/aiohttp)
 - Response models built with [pydantic](https://github.com/samuelcolvin/pydantic)
 - Text validation is implemented through [vbml](https://github.com/tesseradecade/vbml)

## Contributing
You can contribute to the library at any time convenient for you! We are always glad to see your support!

## License
[MIT](./LICENSE) license. **Copyright © 2020 [exthrempty](https://github.com/exthrempty)**