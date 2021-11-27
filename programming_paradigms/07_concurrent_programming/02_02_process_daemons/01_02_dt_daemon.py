"""
Explore the fact that daemonized procs will terminate immediately
when the main process terminates.
"""
import time
import multiprocessing as mp

PROC_WAIT = 3


def do_something() -> None:
    this_proc = mp.current_process()
    print(f"[{this_proc.name}] STARTED", flush=True)

    print(f"[{this_proc.name}] WAIT for {PROC_WAIT}s ...", flush=True)
    time.sleep(PROC_WAIT)

    print(f"[{this_proc.name}] STOP", flush=True)


def main() -> None:
    print("[MAIN] START", flush=True)

    some_proc = mp.Process(
        target=do_something,
        name="maximus"
    )

    some_proc.daemon = True
    some_proc.start()

    print("[MAIN] WAIT for 1s ...")
    time.sleep(1)

    print("[MAIN] DONE", flush=True)


if __name__ == '__main__':
    main()
