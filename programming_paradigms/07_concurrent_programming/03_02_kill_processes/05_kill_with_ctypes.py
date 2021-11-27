import time
import random
import ctypes
import multiprocessing as mp


def do_something(is_running: mp.Value) -> None:
    this_proc = mp.current_process()
    print(f"[{this_proc.name}] STARTED", flush=True)

    print(f"[{this_proc.name}] WAIT ...", flush=True)
    while is_running.value:
        print(f"[{this_proc.name}] DO {random.randint(1, 100)}", flush=True)
        time.sleep(random.random())

    print(f"[{this_proc.name}] DONE", flush=True)


def main() -> None:
    print("[MAIN] START", flush=True)

    is_running = mp.Value(ctypes.c_bool, True)

    some_proc = mp.Process(
        target=do_something,
        name="maximus",
        args=(is_running,)
    )

    some_proc.start()

    print("[MAIN] WAIT 2s ...", flush=True)
    time.sleep(2)

    print("[MAIN] initiate kill ...")
    is_running.value = False

    print("[MAIN] wait for process to DIE ...")
    some_proc.join()

    print("[MAIN] DONE", flush=True)


if __name__ == '__main__':
    main()
