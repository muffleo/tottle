from tottle import Blueprint, Message


# Creating a blueprint object
bp = Blueprint(name="Echo")


@bp.on.message()
async def echo(message: Message):
    return "Your message: " + message.text
