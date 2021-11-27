import time
import random
import threading
import queue

from typing import Any


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

    stop_queue: queue.Queue[Any] = queue.Queue()

    some_thread = threading.Thread(
        target=do_something,
        name="maximus",
        args=(stop_queue,)
    )

    some_thread.start()

    print("[MAIN] WAIT for 2s ...", flush=True)
    time.sleep(2)

    print("[MAIN] initiate stop ...", flush=True)
    stop_queue.put(None)  # only one because we have only one thread

    print("[MAIN] wait for child thread to DIE")
    some_thread.join()

    print("[MAIN] DONE", flush=True)


if __name__ == '__main__':
    main()
