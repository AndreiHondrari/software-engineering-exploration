import time
import random
import threading
import queue
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


def do_this(val: int) -> None:
    tprint(f"DOES THIS {val}")


def do_that(val: int) -> None:
    tprint(f"DOES THAT {val}")


@mark_thread_ends
def do_send(
    values_queue: queue.Queue[int],
    stop_event: threading.Event
) -> None:

    while not stop_event.is_set():
        values_queue.put(random.randint(1000, 10_000))
        time.sleep(random.random())


@mark_thread_ends
def do_dispatch(
    values_queue: queue.Queue[int],
    stop_event: threading.Event
) -> None:

    while not stop_event.is_set():
        val = values_queue.get()

        if val < 5000:
            do_this(val)
        else:
            do_that(val)


def main() -> None:
    tprint("START\n")

    NO_OF_SENDERS = 10

    values_queue: queue.Queue[int] = queue.Queue()
    stop_event = threading.Event()

    tprint("Create senders ...")
    senders = []
    for i in range(NO_OF_SENDERS):
        new_sender = threading.Thread(
            target=do_send,
            args=(values_queue, stop_event,)
        )
        senders.append(new_sender)

    tprint("Create dispatcher ...")
    dispatcher = threading.Thread(
        target=do_dispatch,
        args=(values_queue, stop_event,)
    )
    dispatcher.daemon = True

    try:
        tprint("Start threads")
        dispatcher.start()
        for sender in senders:
            sender.start()

        tprint("Wait for threads ...")
        for sender in senders:
            sender.join()
        dispatcher.join()
    except KeyboardInterrupt:
        tprint("\nInterrupt detected")
        stop_event.set()
    finally:
        tprint("Final wait")
        for sender in senders:
            sender.join(2)

    tprint("\nDONE")


if __name__ == '__main__':
    main()
