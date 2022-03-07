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


def do_killing(stop_event: threading.Event) -> None:
    this_thread = threading.current_thread()
    print(f"[{this_thread.name}] STARTED", flush=True)

    print(f"[{this_thread.name}] WAIT 2s...", flush=True)
    time.sleep(2)

    print(f"[{this_thread.name}] initiating kill...", flush=True)
    stop_event.set()

    print(f"[{this_thread.name}] STOP", flush=True)


def main() -> None:
    print("[MAIN] START", flush=True)

    stop_event = threading.Event()

    # create threads
    some_thread = threading.Thread(
        target=do_something,
        name="maximus",
        args=(stop_event,)
    )
    killer_thread = threading.Thread(
        target=do_killing,
        name="killer",
        args=(stop_event,)
    )

    # start threads
    print("[MAIN] start threads")
    some_thread.start()
    killer_thread.start()

    print("[MAIN] wait for child threads to DIE")
    killer_thread.join()
    some_thread.join()

    print("[MAIN] DONE", flush=True)


if __name__ == '__main__':
    main()
