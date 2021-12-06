
import random
import asyncio
import functools
import threading

from typing import Any, Callable


def tprint(msg: str) -> None:
    this_thread = threading.current_thread()
    print(f"[{this_thread.name}] {msg}", flush=True)


def mark_thread_ends(
    do_func: Callable[..., Any]
) -> Callable[..., Any]:

    @functools.wraps(do_func)
    def _inner(*args: Any, **kwargs: Any) -> Any:
        tprint("START")
        ret = do_func(*args, **kwargs)
        tprint("STOP")
        return ret

    return _inner


async def do_something() -> int:
    print("START DO SOMETHING")
    await asyncio.sleep(1)
    print("DONE WAITING")

    return random.randint(1000, 10_000)


async def asynchronous_main() -> None:
    loop = asyncio.get_event_loop()
    tprint(repr(loop))
    for x in dir(loop):
        if x[:2] != '__':
            tprint(f"loop.{x}")


@mark_thread_ends
def main() -> None:
    asyncio.run(asynchronous_main())  # run main in an event loop


if __name__ == '__main__':
    main()
