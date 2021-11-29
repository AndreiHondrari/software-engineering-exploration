"""
Livelock

Detect by checking the state of both events after a while
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


@mark_thread_ends
def do_something(
    lock: threading.Lock,
    partner_used_resource_event: threading.Event,
    own_used_resource_event: threading.Event,
) -> None:

    tprint("allow the other party to use it at least once")
    while not partner_used_resource_event.is_set():
        tprint("wait for the partner to use resource")
        time.sleep(0.5)

    tprint("other party has used resource, proceed with using it ourselves")
    lock.acquire()
    tprint("lock acquired")

    own_used_resource_event.set()

    tprint("release lock")
    lock.release()
    tprint("lock released")


@mark_thread_ends
def do_livelock_detection(
    signal_a: threading.Event,
    signal_b: threading.Event,
) -> None:

    tprint("wait for the threads to do their thing ...")
    TIMEOUT = 1
    time.sleep(TIMEOUT)

    tprint("perform detection")
    if not signal_a.is_set() and not signal_b.is_set():
        tprint("LIVELOCK DETECTED")


@mark_thread_ends
def main() -> None:

    lock = threading.Lock()

    thread_a_used_resource_event = threading.Event()
    thread_b_used_resource_event = threading.Event()

    tprint("create threads")
    thread_a = threading.Thread(
        target=do_something,
        name="maximus",
        args=(
            lock,
            thread_b_used_resource_event,  # partner
            thread_a_used_resource_event,  # owner
        )
    )
    thread_a.daemon = True

    thread_b = threading.Thread(
        target=do_something,
        name="gandalf",
        args=(
            lock,
            thread_a_used_resource_event,  # partner
            thread_b_used_resource_event,  # owner
        )
    )
    thread_b.daemon = True

    detective = threading.Thread(
        target=do_livelock_detection,
        name="detective",
        args=(
            thread_b_used_resource_event,
            thread_a_used_resource_event,
        )
    )
    detective.daemon = True

    tprint("start threads")
    detective.start()
    thread_a.start()
    thread_b.start()

    tprint("wait for threads to DIE ...")
    MAX_TIMEOUT = 2
    detective.join(timeout=MAX_TIMEOUT)
    thread_a.join(timeout=MAX_TIMEOUT)
    thread_b.join(timeout=MAX_TIMEOUT)


if __name__ == '__main__':
    main()
