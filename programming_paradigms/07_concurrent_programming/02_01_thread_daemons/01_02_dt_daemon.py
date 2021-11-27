"""
Explore the fact that daemonized threads will terminate immediately
when the main process terminates.
"""
import time
import threading

THREAD_WAIT = 3


def do_something() -> None:
    this_thread = threading.current_thread()
    print(f"[{this_thread.name}] STARTED", flush=True)

    print(f"[{this_thread.name}] WAIT for {THREAD_WAIT}s ...", flush=True)
    time.sleep(THREAD_WAIT)

    print(f"[{this_thread.name}] STOP", flush=True)


def main() -> None:
    print("[MAIN] START", flush=True)

    some_thread = threading.Thread(
        target=do_something,
        name="maximus"
    )

    some_thread.daemon = True
    some_thread.start()

    print("[MAIN] WAIT for 1s ...")
    time.sleep(1)

    print("[MAIN] DONE", flush=True)


if __name__ == '__main__':
    main()
