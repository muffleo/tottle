from tottle import Bot, Message
from tottle.exception_factory import swear


bot = Bot(token="Your token")


def zero_division_handler(exc: ZeroDivisionError):
    print("Can't be divided by zero!")


# Using the decorator, we specify the type of error and the function that will be triggered when an error occurs
# This error will only be handled in the function to which you applied the decorator
@swear(
    exception=ZeroDivisionError,
    exception_handler=zero_division_handler
)
def zero_division() -> str:
    a = 1 / 0

    return str(a)


@bot.on.message()
async def answer(message: Message):
    zero_division()


bot.run_forever()
