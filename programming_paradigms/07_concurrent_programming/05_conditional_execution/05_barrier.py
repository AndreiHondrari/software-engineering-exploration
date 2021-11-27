import time
import random
import threading

from typing import List


def do_something(barrier: threading.Barrier) -> None:
    this_thread = threading.current_thread()
    tname = this_thread.name
    print(f"[{tname}] START", flush=True)

    MIN_WAIT = 1
    MAX_WAIT = 3
    wait_time = round(random.random() * (MAX_WAIT - MIN_WAIT) + MIN_WAIT, 2)
    print(f"[{tname}] wait {wait_time}", flush=True)
    time.sleep(wait_time)

    print(f"[{tname}] got to barrier", flush=True)
    rc = barrier.wait()

    print(f"[{tname}] barrier passed | RC: {rc}", flush=True)

    print(f"[{tname}] STOP", flush=True)


def main() -> None:
    print("[MAIN] START", flush=True)

    NO_OF_THREADS = 3

    barrier = threading.Barrier(parties=NO_OF_THREADS)
    thread_collection: List[threading.Thread] = []

    print("[MAIN] create threads", flush=True)
    for i in range(NO_OF_THREADS):
        new_thread = threading.Thread(
            target=do_something,
            name=f"T-{i}",
            args=(barrier,)
        )
        thread_collection.append(new_thread)

    print("[MAIN] start threads", flush=True)
    for i in range(NO_OF_THREADS):
        thread_collection[i].start()

    print("[MAIN] wait for threads", flush=True)
    for i in range(NO_OF_THREADS):
        thread_collection[i].join()

    print("[MAIN] STOP", flush=True)


if __name__ == '__main__':
    main()
