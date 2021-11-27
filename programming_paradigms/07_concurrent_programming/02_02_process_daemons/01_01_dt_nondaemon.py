"""
Explore the fact that non-daemonized procs will keep the
main process alive until it finished.
"""
import time
import multiprocessing as mp


def do_something() -> None:
    this_proc = mp.current_process()
    print(f"[{this_proc.name}] STARTED", flush=True)

    print(f"[{this_proc.name}] WAIT ...", flush=True)
    time.sleep(2)

    print(f"[{this_proc.name}] STOP", flush=True)


def main() -> None:
    print("[MAIN] START", flush=True)

    some_proc = mp.Process(
        target=do_something,
        name="maximus"
    )

    some_proc.start()

    print("[MAIN] DONE", flush=True)


if __name__ == '__main__':
    main()
