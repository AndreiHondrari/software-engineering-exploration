
import time
import asyncio
import functools
import threading

from typing import Any, Callable


def tprint(*args: Any) -> None:
    this_thread = threading.current_thread()

    msg_parts = [f"[{this_thread.name}] "]
    msg_parts += [str(x) for x in args]
    msg = "".join(msg_parts) + "\n"
    print(msg, flush=True, end="")


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


@mark_thread_ends
def do_blocking_action() -> None:
    for i in range(3):
        tprint(i)
        time.sleep(0.5)


async def do_dispatching() -> None:
    blocking_task_1 = asyncio.to_thread(do_blocking_action)
    blocking_task_2 = asyncio.to_thread(do_blocking_action)

    await asyncio.gather(blocking_task_1, blocking_task_2)


@mark_thread_ends
def main() -> None:
    asyncio.run(do_dispatching())


if __name__ == '__main__':
    main()
