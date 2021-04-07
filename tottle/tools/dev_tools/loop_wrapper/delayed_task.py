from asyncio import sleep
from typing import Callable, Coroutine, Any

Handler = Callable[..., Coroutine[Any, Any, Any]]


async def delayed_task(
        seconds: int,
        handler: Handler,
        do_break: bool = False,
        *args,
        **kwargs
):
    while True:
        await sleep(seconds)
        await handler(*args, **kwargs)

        if do_break:
            break
