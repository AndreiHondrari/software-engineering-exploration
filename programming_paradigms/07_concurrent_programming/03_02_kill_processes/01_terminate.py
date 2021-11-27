"""
This method is extreme and can cause problems with unreleased locks
and can corrupt queues or pipes.
"""
import time
import random
import multiprocessing as mp


def do_something() -> None:
    this_proc = mp.current_process()
    print(f"[{this_proc.name}] STARTED", flush=True)

    print(f"[{this_proc.name}] WAIT ...", flush=True)
    while True:
        print(f"[{this_proc.name}] DO {random.randint(1, 100)}", flush=True)
        time.sleep(random.random())


def main() -> None:
    print("[MAIN] START", flush=True)

    some_proc = mp.Process(
        target=do_something,
        name="maximus"
    )

    some_proc.start()

    print("[MAIN] WAIT 2s ...", flush=True)
    time.sleep(2)

    print("[MAIN] initiate termination ...")
    some_proc.terminate()

    print("[MAIN] DONE", flush=True)


if __name__ == '__main__':
    main()
