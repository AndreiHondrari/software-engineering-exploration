import time
import random
import multiprocessing as mp


def do_something(stop_event: mp.Event) -> None:
    this_proc = mp.current_process()
    print(f"[{this_proc.name}] STARTED", flush=True)

    print(f"[{this_proc.name}] WAIT ...", flush=True)
    while not stop_event.is_set():

        print(f"[{this_proc.name}] DO {random.randint(1, 100)}", flush=True)
        time.sleep(random.random())

    print(f"[{this_proc.name}] DONE", flush=True)


def main() -> None:
    print("[MAIN] START", flush=True)

    stop_event = mp.Event()

    some_proc = mp.Process(
        target=do_something,
        name="maximus",
        args=(stop_event,)
    )

    some_proc.start()

    print("[MAIN] WAIT 2s ...", flush=True)
    time.sleep(2)

    print("[MAIN] initiate kill ...")
    stop_event.set()

    print("[MAIN] wait for process to DIE ...")
    some_proc.join()

    print("[MAIN] DONE", flush=True)


if __name__ == '__main__':
    main()
