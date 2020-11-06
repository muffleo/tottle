<h1 align="center">Tottle — fast, async & powerful Telegram API wrapper</h1>

<p align="center">
    <img src="https://img.shields.io/github/license/muffleo/tottle">
    <a href="https://t.me/joinchat/S_jqPkv4GVNEb4Z70MI6vQ">
        <img src="https://img.shields.io/badge/Telegram%20Chat-join-informational" alt="Telegram Chat — join us!">
    </a>
</p>


### 🔗 Installation
1) From **GitHub**:
    ```sh
   pip install -U https://github.com/muffleo/tottle/archive/master.zip
   ```
   
### ⚙ Examples
#### "Hello, World!" example
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

### 🛠 Using
 - Based on [vkbottle](https://github.com/timoniq/vkbottle)
 - Powered by [aiohttp](https://github.com/aio-libs/aiohttp)
 - Response models built with [pydantic](https://github.com/samuelcolvin/pydantic)
 - Text validation is implemented through [vbml](https://github.com/tesseradecade/vbml)

### ⭐ Contributing
Because the whole library is not actually completed, we are always glad to see your support. This is a list of our current goals:

| Plan to add    | In progress              | Completed                  |
|----------------|--------------------------|----------------------------|
| FSM            | API and its object types | Middlewares                |
| Return Manager | HTTP Client              | Polling                    |
| Blueprints     |                          | Generating (keyboard etc.) |