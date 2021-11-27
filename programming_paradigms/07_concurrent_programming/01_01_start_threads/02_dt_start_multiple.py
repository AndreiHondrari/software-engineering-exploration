import time
import random
import threading
from typing import List


def do_something() -> None:
    this_thread = threading.current_thread()
    print(f"[{this_thread.name}] STARTED")

    for i in range(3):
        print(f"[{this_thread.name}] {random.randint(1, 1000)}")
        time.sleep(random.random())

    print(f"[{this_thread.name}] STOPPED")


def main() -> None:
    print("[MAIN] START")

    NO_OF_THREADS = 3
    threads_collection: List[threading.Thread] = []

    # create threads
    for i in range(NO_OF_THREADS):
        new_thread_code = random.randint(1000, 10_000)

        new_thread = threading.Thread(
            target=do_something,
            name=str(new_thread_code)
        )
        threads_collection.append(new_thread)

    # start threads
    for i in range(NO_OF_THREADS):
        threads_collection[i].start()

    # wait for threads to finish
    for i in range(NO_OF_THREADS):
        threads_collection[i].join()

    print("[MAIN] DONE")


if __name__ == '__main__':
    main()
