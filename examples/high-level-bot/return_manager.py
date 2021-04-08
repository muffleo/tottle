from tottle import Bot, Message


bot = Bot(token="Your token")


@bot.on.message(text="return str")
async def return_str(message: Message):
    # Returns a message whose text is equal to the return value
    return "Returning the string works successfully!"


@bot.on.message(text="return list")
async def return_list(message: Message):
    # Returns multiple messages with text from the list
    # You can use both lists and tuples
    return ["Hello!", "How are you today?"]


@bot.on.message(text="return dict")
async def return_dict(message: Message):
    # Returns a message with the parameters specified as keys in the dictionary
    # Output: Good to see you!
    return {"text": "Good to see you!"}


bot.run_forever()
