import time
import threading

from typing import List


def do_something(some_condition: threading.Condition) -> None:
    this_thread = threading.current_thread()
    tname = this_thread.name
    print(f"[{tname}] START", flush=True)

    print(f"[{tname}] wait for condition ...", flush=True)
    some_condition.acquire()
    some_condition.wait()
    some_condition.release()

    print(f"[{tname}] condition passed!", flush=True)

    print(f"[{tname}] STOP", flush=True)


def main() -> None:
    print("[MAIN] START")

    NO_OF_THREADS = 3
    thread_collection: List[threading.Thread] = []

    some_condition = threading.Condition()

    print("[MAIN] create threads")
    for i in range(NO_OF_THREADS):
        new_thread = threading.Thread(
            target=do_something,
            name=f"T-{i}",
            args=(some_condition,)
        )
        thread_collection.append(new_thread)

    print("[MAIN] start threads")
    for i in range(NO_OF_THREADS):
        thread_collection[i].start()

    print("[MAIN] wait 2s ...")
    time.sleep(2)

    HOW_MANY = 2
    print(f"[MAIN] signal continue to {HOW_MANY} threads")
    with some_condition:
        some_condition.notify(n=HOW_MANY)

    print("[MAIN] wait 1s ...")
    time.sleep(1)

    print("[MAIN] signal continue to last thread")
    with some_condition:
        some_condition.notify()

    print("[MAIN] wait for all threads to finish")
    for i in range(NO_OF_THREADS):
        thread_collection[i].join()

    print("[MAIN] STOP")


if __name__ == '__main__':
    main()
