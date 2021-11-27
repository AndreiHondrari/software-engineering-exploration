import os
import time
import random
import threading
import signal


def do_something() -> None:
    this_thread = threading.current_thread()
    print(f"[{this_thread.name}] STARTED", flush=True)

    print(f"[{this_thread.name}] DO STUFF", flush=True)

    try:
        while True:
            print(f"[{this_thread.name}] {random.randint(1, 100)}", flush=True)
            time.sleep(random.random())
    except KeyboardInterrupt:
        print(f"[{this_thread.name}] INTERUPT DETECTED")

    print(f"[{this_thread.name}] STOP", flush=True)


def main() -> None:
    print("[MAIN] START", flush=True)
    print("[MAIN] PID", os.getpid(), flush=True)

    some_thread = threading.Thread(
        target=do_something,
        name="maximus",
    )

    some_thread.start()

    print("[MAIN] WAIT for 2s ...", flush=True)
    time.sleep(2)

    print("[MAIN] initiate stop ...", flush=True)
    main_thread = threading.main_thread()
    if main_thread.ident is not None:
        signal.pthread_kill(main_thread.ident, signal.SIGKILL)
    else:
        print("[MAIN] Abnormal inexistence of ident value for main thread")

    print("[MAIN] wait for child thread to DIE")
    some_thread.join()

    print("[MAIN] DONE", flush=True)


if __name__ == '__main__':
    main()
