"""
Explore the fact that non-daemonized threads will keep the
main process alive until it finished.
"""
import time
import threading


def do_something() -> None:
    this_thread = threading.current_thread()
    print(f"[{this_thread.name}] STARTED", flush=True)

    print(f"[{this_thread.name}] WAIT ...", flush=True)
    time.sleep(2)

    print(f"[{this_thread.name}] STOP", flush=True)


def main() -> None:
    print("[MAIN] START", flush=True)

    some_thread = threading.Thread(
        target=do_something,
        name="maximus"
    )

    some_thread.start()

    print("[MAIN] DONE", flush=True)


if __name__ == '__main__':
    main()
