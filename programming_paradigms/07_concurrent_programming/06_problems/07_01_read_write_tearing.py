"""
Read/write tearing

Reading and writing very fast from a global variable of a large size,
results in non-deterministic behaviour as to why the thread that writes
does not have time to properly store the bits in the variable,
while in the meantime it is read and stored locally with a corrupted and
incomplete value.
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


k = 0


@mark_thread_ends
def do_write(
    stop_event: threading.Event
) -> None:
    global k

    flip = False
    while not stop_event.is_set():
        k = 0x0 if flip else 0xaaabbbbccccdddd
        flip = not flip


@mark_thread_ends
def do_read(
    stop_event: threading.Event
) -> None:
    global k

    while not stop_event.is_set():
        res = k == 0x0 or k == 0xaaabbbbccccdddd
        if not res:
            tprint("FAULT DETECTED")


@mark_thread_ends
def main() -> None:
    stop_event = threading.Event()

    tprint("create threads")
    writer = threading.Thread(
        target=do_write,
        name="writer",
        args=(stop_event,)
    )
    writer.daemon = True

    reader = threading.Thread(
        target=do_read,
        name="reader",
        args=(stop_event,)
    )
    reader.daemon = True

    tprint("start threads")
    writer.start()
    reader.start()

    tprint("wait for threads to DIE ...")
    try:
        writer.join()
        reader.join()
    except KeyboardInterrupt:
        print("\nStop detected")
    finally:
        print("closing ...")
        stop_event.set()
        writer.join()
        reader.join()


if __name__ == '__main__':
    main()
