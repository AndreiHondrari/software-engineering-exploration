import time
import random
import threading
import queue

from typing import List, Any


def do_something(stop_queue: queue.Queue[Any]) -> None:
    this_thread = threading.current_thread()
    print(f"[{this_thread.name}] STARTED", flush=True)

    print(f"[{this_thread.name}] DO STUFF", flush=True)
    while True:
        if not stop_queue.empty():
            stop_queue.get()
            break

        print(f"[{this_thread.name}] {random.randint(1, 100)}", flush=True)
        time.sleep(random.random())

    stop_queue.task_done()
    print(f"[{this_thread.name}] STOP", flush=True)


def main() -> None:
    print("[MAIN] START", flush=True)

    NO_OF_WORKERS = 3

    workers_collection: List[threading.Thread] = []
    stop_queue: queue.Queue[Any] = queue.Queue()

    # create workers
    for i in range(NO_OF_WORKERS):
        new_thread = threading.Thread(
            target=do_something,
            name=f"T_{i+1:0<4}",
            args=(stop_queue,)
        )
        workers_collection.append(new_thread)

    # start workers
    for i in range(NO_OF_WORKERS):
        workers_collection[i].start()

    print("[MAIN] WAIT for 2s ...", flush=True)
    time.sleep(2)

    print("[MAIN] initiate stop ...", flush=True)
    for i in range(NO_OF_WORKERS):
        stop_queue.put(None)  # one put for each worker

    print("[MAIN] wait for child threads to DIE")
    for i in range(NO_OF_WORKERS):
        workers_collection[i].join()

    print("[MAIN] DONE", flush=True)


if __name__ == '__main__':
    main()
