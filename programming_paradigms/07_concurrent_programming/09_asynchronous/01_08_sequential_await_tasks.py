
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


async def do_something(
    name: str,
    wait_time: int
) -> int:
    tprint(f"[{name}] START DO SOMETHING")
    await asyncio.sleep(wait_time)
    tprint(f"[{name}] DONE WAITING")

    return random.randint(1000, 10_000)


async def asynchronous_main() -> None:
    tprint("Create task 1")
    task1 = asyncio.create_task(do_something("jimmy", 2))

    tprint("Create task 2")
    task2 = asyncio.create_task(do_something("maximus", 2))

    result: int

    tprint("Await for task 1")
    result = await task1
    tprint(f"Result 1: {result}")

    tprint("Await for task 2")
    result = await task2
    tprint(f"Result 2: {result}")

    tprint("DONE")


def main() -> None:
    asyncio.run(asynchronous_main())  # run main in an event loop


if __name__ == '__main__':
    main()
