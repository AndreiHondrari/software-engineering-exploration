import time
import threading


def do_something(lock: threading.Lock) -> None:
    this_thread = threading.current_thread()
    tname = this_thread.name
    print(f"[{tname}] START", flush=True)

    print(f"[{tname}] first lock acquire attempt ...", flush=True)
    lock.acquire()
    print(f"[{tname}] first lock acquired !", flush=True)

    print(f"[{tname}] second lock acquire attempt ...", flush=True)
    lock.acquire()
    print(f"[{tname}] second lock acquired !", flush=True)

    print(
        f"[{tname}] wait 2s so the other thread attempts acquire ...",
        flush=True
    )
    time.sleep(2)

    print(f"[{tname}] lock release", flush=True)
    while True:
        try:
            lock.release()
            print(f"[{tname}] released", flush=True)
        except RuntimeError:
            print(f"[{tname}] no more releases left")
            break

    print(f"[{tname}] STOP", flush=True)


def do_something_else(lock: threading.Lock) -> None:
    this_thread = threading.current_thread()
    tname = this_thread.name
    print(f"[{tname}] START", flush=True)

    print(f"[{tname}] wait 1s so the other thread can acquire...", flush=True)
    time.sleep(1)

    print(f"[{tname}] lock acquire attempt ...", flush=True)
    lock.acquire()
    print(f"[{tname}] lock acquired !", flush=True)

    print(f"[{tname}] lock release", flush=True)
    lock.release()

    print(f"[{tname}] STOP", flush=True)


def main() -> None:
    print("[MAIN] START", flush=True)

    lock = threading.RLock()

    print("[MAIN] create threads", flush=True)
    some_thread = threading.Thread(
        target=do_something,
        name="maximus",
        args=(lock,)
    )

    some_other_thread = threading.Thread(
        target=do_something_else,
        name="gandalf",
        args=(lock,)
    )

    print("[MAIN] start threads", flush=True)
    some_thread.start()
    some_other_thread.start()

    print("[MAIN] wait for threads", flush=True)
    some_thread.join()
    some_other_thread.join()

    print("[MAIN] STOP", flush=True)


if __name__ == '__main__':
    main()
