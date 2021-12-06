
import time
import random
import asyncio
import functools
import threading

from typing import Any, Callable


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
    for i in range(3):
        tprint(f"[{name}] {i}")
        time.sleep(0.5)

    tprint(f"[{name}] FINALLY WAIT")
    await asyncio.sleep(wait_time)
    tprint(f"[{name}] DONE WAITING")

    return random.randint(1000, 10_000)


@mark_thread_ends
def main() -> None:

    tprint("Create an event loop")
    loop = asyncio.new_event_loop()

    tprint("Create a task with the loop")
    task = loop.create_task(do_something("jimmy", 1))

    tprint("Run the task in the loop")
    loop.run_until_complete(task)


if __name__ == '__main__':
    main()
