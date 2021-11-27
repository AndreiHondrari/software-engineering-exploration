import time
import random
import threading

from typing import List


def do_something(stop_event: threading.Event) -> None:
    this_thread = threading.current_thread()
    print(f"[{this_thread.name}] STARTED", flush=True)

    print(f"[{this_thread.name}] DO STUFF", flush=True)
    while not stop_event.is_set():
        print(f"[{this_thread.name}] {random.randint(1, 100)}", flush=True)
        time.sleep(random.random())

    print(f"[{this_thread.name}] STOP", flush=True)


def main() -> None:
    print("[MAIN] START", flush=True)

    NO_OF_WORKERS = 3

    workers_collection: List[threading.Thread] = []
    stop_event = threading.Event()

    # create workers
    for i in range(NO_OF_WORKERS):
        new_thread = threading.Thread(
            target=do_something,
            name=f"T_{i+1:0<4}",
            args=(stop_event,)
        )
        workers_collection.append(new_thread)

    # start workers
    for i in range(NO_OF_WORKERS):
        workers_collection[i].start()

    print("[MAIN] WAIT for 2s ...", flush=True)
    time.sleep(2)

    print("[MAIN] initiate stop ...", flush=True)
    stop_event.set()

    print("[MAIN] wait for children threads to DIE")
    for i in range(NO_OF_WORKERS):
        workers_collection[i].join()

    print("[MAIN] DONE", flush=True)


if __name__ == '__main__':
    main()
