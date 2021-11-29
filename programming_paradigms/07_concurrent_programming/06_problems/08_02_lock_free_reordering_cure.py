"""
Lock-free reordering
"""
import threading
import functools

from typing import Callable, Any


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


x = 0
y = 0
a = 0
b = 0


@mark_thread_ends
def do_this(memory_barrier: threading.Barrier) -> None:
    global x
    global y
    global a

    y = 1
    memory_barrier.wait()
    x = a


@mark_thread_ends
def do_that(memory_barrier: threading.Barrier) -> None:
    global x
    global y
    global b

    x = 1
    memory_barrier.wait()
    y = b


@mark_thread_ends
def main() -> None:

    memory_barrier = threading.Barrier(2)

    tprint("create threads")
    thread_1 = threading.Thread(
        target=do_this,
        name="thread_1",
        args=(memory_barrier,)
    )
    thread_1.daemon = True

    thread_2 = threading.Thread(
        target=do_that,
        name="thread_2",
        args=(memory_barrier,)
    )
    thread_2.daemon = True

    tprint("start threads")
    thread_1.start()
    thread_2.start()

    tprint("wait for threads to DIE ...")
    thread_1.join()
    thread_2.join()

    print("x", x)
    print("y", y)


if __name__ == '__main__':
    main()
