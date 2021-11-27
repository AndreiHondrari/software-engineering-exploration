"""
Semaphores are useful when we want to limit the number of
threads that are accessing a resource in parallel.

Examples:
- only 5 connections per database
- only 5 sessions per TCP socket
"""
import time
import threading

from typing import List


def do_something(semaphore: threading.Semaphore) -> None:
    this_thread = threading.current_thread()
    tname = this_thread.name
    print(f"[{tname}] START", flush=True)

    print(f"[{tname}] LOOPING", flush=True)
    for i in range(3):
        print(f"[{tname}] try acquire", flush=True)
        semaphore.acquire()
        print(f"[{tname}] acquired", flush=True)

        print(f"[{tname}] DO for 1s", flush=True)
        time.sleep(1)

        print(f"[{tname}] release", flush=True)
        semaphore.release()

    print(f"[{tname}] STOP", flush=True)


def main() -> None:
    print("[MAIN] START", flush=True)

    semaphore = threading.Semaphore(value=2)

    NO_OF_THREADS = 3
    thread_collection: List[threading.Thread] = []

    print("[MAIN] create threads", flush=True)
    for i in range(NO_OF_THREADS):
        new_thread = threading.Thread(
            target=do_something,
            name=f"T-{i}",
            args=(semaphore,)
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
