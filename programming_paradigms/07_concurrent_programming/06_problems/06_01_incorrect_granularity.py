"""
Incorrect granularity

Assuming that two independent operations are thread-safe and using them
together could result in an unsafe
"""

import time
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


resource_x = 0
resource_y = 0


@mark_thread_ends
def do_update(
    x_lock: threading.Lock,
    y_lock: threading.Lock,
    stop_event: threading.Event
) -> None:
    global resource_x
    global resource_y

    INCR = 11

    while not stop_event.is_set():
        tprint("update x")
        x_lock.acquire()
        resource_x += INCR
        x_lock.release()

        tprint("fake wait")
        time.sleep(1)

        tprint("update y")
        y_lock.acquire()
        resource_y += INCR
        y_lock.release()

        time.sleep(0.001)


@mark_thread_ends
def do_balance_check(
    x_lock: threading.Lock,
    y_lock: threading.Lock,
    stop_event: threading.Event
) -> None:
    global resource_x
    global resource_y

    tprint("Loop for checking")
    while not stop_event.is_set():
        x_lock.acquire()
        y_lock.acquire()
        difference = abs(resource_x - resource_y)
        x_lock.release()
        y_lock.release()

        if difference == 0:
            tprint("balance is OK")
        else:
            tprint("DETECTED IMBALANCE")

        time.sleep(0.5)


@mark_thread_ends
def main() -> None:

    x_lock = threading.Lock()
    y_lock = threading.Lock()
    stop_event = threading.Event()

    tprint("create threads")
    updater = threading.Thread(
        target=do_update,
        name="updater",
        args=(x_lock, y_lock, stop_event,)
    )
    updater.daemon = True

    checker = threading.Thread(
        target=do_balance_check,
        name="checker",
        args=(x_lock, y_lock, stop_event,)
    )
    checker.daemon = True

    tprint("start threads")
    updater.start()
    checker.start()

    tprint("let threads do some work")
    time.sleep(3)
    stop_event.set()

    tprint("wait for threads to finish")
    updater.join()
    checker.join()


if __name__ == '__main__':
    main()
