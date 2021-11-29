"""
Livelock

Threads keep relinquishing their control to the others peers
rendering the whole system in a state of actively doing without any progress
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

    tprint("start threads")
    thread_a.start()
    thread_b.start()

    tprint("wait for threads to DIE ...")
    MAX_TIMEOUT = 2
    thread_a.join(timeout=MAX_TIMEOUT)
    thread_b.join(timeout=MAX_TIMEOUT)

    # check livelock
    if (
        not thread_a_used_resource_event.is_set() and
        not thread_b_used_resource_event.is_set()
    ):
        tprint("LIVELOCK DETECTED")
    else:
        tprint("at least one of the the threads made it ! :) ")


if __name__ == '__main__':
    main()
