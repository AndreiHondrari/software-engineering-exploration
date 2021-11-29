"""
Resource depletion.

A thread will take all the resources and not release them while finishing.
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
def do_slow_achieve(
    semaphore: threading.Semaphore,
    acquired_resource_event: threading.Event
) -> None:
    tprint("be slow -> wait for 1s ...")
    time.sleep(1)

    tprint("try to acquire any resources")
    semaphore.acquire()
    acquired_resource_event.set()

    tprint("acquired, now do something")
    time.sleep(1)

    semaphore.release()


@mark_thread_ends
def do_greedy(
    semaphore: threading.Semaphore,
) -> None:
    tprint("acquire EVERYTHING")
    while True:
        result = semaphore.acquire(blocking=False)
        if not result:
            break


@mark_thread_ends
def do_resource_depletion_detection(
    acquired_resource_event: threading.Event
) -> None:
    tprint("wait for threads to do their thing")
    TIMEOUT = 1
    time.sleep(TIMEOUT)

    if not acquired_resource_event.is_set():
        tprint("RESOURCE DEPLETION DETECTED")


@mark_thread_ends
def main() -> None:
    semaphore = threading.Semaphore(value=3)
    slow_threads_acquired_resource = threading.Event()

    tprint("create threads")
    detective = threading.Thread(
        target=do_resource_depletion_detection,
        name="detective",
        args=(slow_threads_acquired_resource,)
    )
    detective.daemon = True

    slow_thread_1 = threading.Thread(
        target=do_slow_achieve,
        name="slime",
        args=(semaphore, slow_threads_acquired_resource,)
    )
    slow_thread_1.daemon = True

    slow_thread_2 = threading.Thread(
        target=do_slow_achieve,
        name="slug",
        args=(semaphore, slow_threads_acquired_resource,)
    )
    slow_thread_2.daemon = True

    greedy_thread = threading.Thread(
        target=do_greedy,
        name="GRINCH",
        args=(semaphore,)
    )
    greedy_thread.daemon = True

    tprint("start treads")
    detective.start()
    slow_thread_1.start()
    slow_thread_2.start()
    greedy_thread.start()

    tprint("wait for threads to DIE ...")
    MAX_TIMEOUT = 1.5
    detective.join(timeout=MAX_TIMEOUT)
    slow_thread_1.join(timeout=MAX_TIMEOUT)
    slow_thread_2.join(timeout=MAX_TIMEOUT)
    greedy_thread.join(timeout=MAX_TIMEOUT)

    if slow_threads_acquired_resource.is_set():
        tprint("one of the slow threads made it \\:D/ !")
    else:
        tprint("NONE of the slow threads made it :( !")


if __name__ == '__main__':
    main()
