from tottle import Bot, Message


bot = Bot(token="Your token")


def zero_division_handler(exc: ZeroDivisionError):
    print("Can't be divided by zero!")


@bot.on.message()
async def answer(message: Message):
    a = 1 / 0

    await message.answer(str(a))


# Register the error handler with an indication of the function that will handle the error
# Now, every time the specified error occurs, the zero_division_handler function will be called (Check line 13)
bot.error_handler.register_error_handler(
    exception_type=ZeroDivisionError,
    exception_handler=zero_division_handler
)
bot.run_forever()
