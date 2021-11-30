"""
Lock convoy

If there is a hot lock that has to be acquired and released very frequent,
a large number of threads competing to acquire the lock will actually
slow down the overall execution and/or create a bottleneck for a queue
of incoming requests.
"""
import time
import threading
import functools

from typing import Callable, Any, List


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


def do_something(
    target: int,
    lock: threading.Lock,
) -> None:

    for i in range(target):
        lock.acquire()
        lock.release()


def launch_for(
    number_of_threads: int,
    target: int,
    name: str
) -> None:
    print(flush=True)
    tprint(f"Launch {name} | {number_of_threads} threads | {target} ops")
    hot_lock = threading.Lock()

    tprint(f"[{name}] create threads")
    threads: List[threading.Thread] = []

    for i in range(24):
        new_thread = threading.Thread(
            target=do_something,
            args=(target, hot_lock,)
        )
        new_thread.daemon = True
        threads.append(new_thread)

    tprint(f"[{name}] start threads")
    start = time.time()
    for t in threads:
        t.start()

    tprint(f"[{name}] wait for threads to DIE ...")
    for t in threads:
        t.join()

    stop = time.time()
    elapsed_time = stop - start
    tprint(f"[{name}] elapsed time: {elapsed_time:.4f}s")


@mark_thread_ends
def main() -> None:
    try:
        TARGET = 10_000
        launch_for(4, TARGET, "ALFA")
        launch_for(24, TARGET, "BRAVO")
        launch_for(128, TARGET, "CHARLIE")
    except KeyboardInterrupt:
        print(flush=True)
        tprint("Stop detected")


if __name__ == '__main__':
    main()
