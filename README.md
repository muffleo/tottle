<h1 align="center">Tottle — fast, convenient and extensible Telegram API wrapper</h1>

<p align="center">
    <a href="https://vk.me/join/AJQ1d3monBgV17SC1lRCtz1j">
        <img src="https://img.shields.io/badge/VK%20Chat-join-blue" alt="VK Chat — join us!">
    </a>
    <a href="https://t.me/joinchat/S_jqPhhhWD9iDODdMeQx3Q">
        <img src="https://img.shields.io/badge/Telegram%20Chat-join-informational" alt="Telegram Chat — join us!">
    </a>
</p>

<hr>


## Installation
1) From GitHub:
    ```sh
   pip install -U https://github.com/muffleo/tottle/archive/master.zip
   ```
   
## Examples
### Longpoll
In this example, the bot reacts to private messages with the pattern "i love &lt;thing&gt;" and passes the validation result as an argument to the handler (thanks to [vbml](https://github.com/tesseradecade/vbml), it is really easy):
```python
from tottle import Bot, Message
from tottle.dispatch.rules import TextRule

bot = Bot("token-here")

@bot.on.private_message(TextRule("i love <thing>"))
async def wrapper(message: Message, thing: str):
    await message.answer(f"It's great that you love {thing}")

bot.run_polling()
```
You can find more examples in the [examples](./examples) directory.

## Using
 - Based on [vkbottle](https://github.com/timoniq/vkbottle)
 - Powered by [aiohttp](https://github.com/aio-libs/aiohttp)
 - Response models built with [pydantic](https://github.com/samuelcolvin/pydantic)
 - Text validation is implemented through [vbml](https://github.com/tesseradecade/vbml)

## Contributing
You can contribute to the library at any time convenient for you! We are always glad to see your support! This is a list of our current goals:
### Plan to add
- FSM
- Callback updates listening method
### In progress/completed
- Polling
- HTTP client
- Generating (keyboard etc.)
- API and its object types (almost completed)

## License
[MIT](./LICENSE) license. **Copyright © 2020 [Muffle](https://github.com/muffleo)**