
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
    tprint("START DO SOMETHING")
    await asyncio.sleep(1)
    tprint("DONE WAITING")

    return random.randint(1000, 10_000)


async def asynchronous_main() -> None:
    tprint("ASYNC MAIN STARTED")

    tprint("await for do_something")
    result: int = await do_something()
    tprint(f"RESULT: {result}")

    tprint("ASYNC MAIN FINISHED")


@mark_thread_ends
def main() -> None:
    asyncio.run(asynchronous_main())  # run main in an event loop


if __name__ == '__main__':
    main()
