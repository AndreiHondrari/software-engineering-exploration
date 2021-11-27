import time
import random
import multiprocessing as mp
from typing import List


def do_something() -> None:
    this_process = mp.current_process()

    print(f"[{this_process.name}] START")
    print(f"[{this_process.name}] PID: {this_process.pid}")

    for i in range(3):
        print(f"[{this_process.name}] {random.randint(1, 1000)}")
        time.sleep(random.random())

    print(f"[{this_process.name}] STOP")


def main() -> None:
    print("[MAIN] START")

    NO_OF_PROCESSES = mp.cpu_count()
    print(
        f"[MAIN] no of CPU cores (physical cores * virtual cores) "
        f"detected: {NO_OF_PROCESSES}"
    )
    proc_collection: List[mp.Process] = []

    # create processes
    for i in range(NO_OF_PROCESSES):
        new_proc_code = str(random.randint(1000, 10_000))
        new_proc = mp.Process(
            target=do_something,
            name=new_proc_code
        )
        proc_collection.append(new_proc)

    # start processes
    for i in range(NO_OF_PROCESSES):
        proc_collection[i].start()

    # wait for processes to finish
    for i in range(NO_OF_PROCESSES):
        proc_collection[i].join()

    print("[MAIN] DONE")


if __name__ == '__main__':
    main()
