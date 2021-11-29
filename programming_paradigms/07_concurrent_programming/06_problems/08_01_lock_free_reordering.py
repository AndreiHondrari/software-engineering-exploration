"""
Lock-free reordering

You would expect that after the execution both x and y are 0,
but in fact, one of them, or even both, turn out to be 1.

Reason why this is happening is because the interpreter or compiler
choses to reorder the reads and writes for optimisation purposes when
an update to a variable occurs. When the update happens the other thread
notices that there is a newer value.

More on that:
https://docs.microsoft.com/en-us/archive/msdn-magazine/2005/october/understanding-low-lock-techniques-in-multithreaded-apps
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
def do_this() -> None:
    global x
    global y
    global a

    y = 1
    x = a


@mark_thread_ends
def do_that() -> None:
    global x
    global y
    global b

    x = 1
    y = b


@mark_thread_ends
def main() -> None:

    tprint("create threads")
    thread_1 = threading.Thread(
        target=do_this,
        name="thread_1",
    )
    thread_1.daemon = True

    thread_2 = threading.Thread(
        target=do_that,
        name="thread_2",
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
