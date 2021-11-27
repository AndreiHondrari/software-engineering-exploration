import time
import random
import threading


def do_something(stop_event: threading.Event) -> None:
    this_thread = threading.current_thread()
    print(f"[{this_thread.name}] STARTED", flush=True)

    print(f"[{this_thread.name}] DO STUFF", flush=True)
    while not stop_event.is_set():
        print(f"[{this_thread.name}] {random.randint(1, 100)}", flush=True)
        time.sleep(random.random())

    print(f"[{this_thread.name}] STOP", flush=True)


def main() -> None:
    print("[MAIN] START", flush=True)

    stop_event = threading.Event()

    some_thread = threading.Thread(
        target=do_something,
        name="maximus",
        args=(stop_event,)
    )

    some_thread.start()

    print("[MAIN] WAIT for 2s ...", flush=True)
    time.sleep(2)

    print("[MAIN] initiate stop ...", flush=True)
    stop_event.set()

    print("[MAIN] wait for child thread to DIE")
    some_thread.join()

    print("[MAIN] DONE", flush=True)


if __name__ == '__main__':
    main()
