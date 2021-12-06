
import random
import asyncio
import functools
import threading

from typing import Any, Callable, Tuple


def tprint(*args: Any) -> None:
    this_thread = threading.current_thread()
    print(f"[{this_thread.name}]", *args, flush=True)


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
    task1 = asyncio.create_task(do_something("jimmy", 1))

    tprint("Create task 2")
    task2 = asyncio.create_task(do_something("maximus", 1))

    results: Tuple[int, ...] = await asyncio.gather(task1, task2)
    tprint("RESULTS:", results)

    tprint("DONE")


def main() -> None:
    asyncio.run(asynchronous_main())  # run main in an event loop


if __name__ == '__main__':
    main()
