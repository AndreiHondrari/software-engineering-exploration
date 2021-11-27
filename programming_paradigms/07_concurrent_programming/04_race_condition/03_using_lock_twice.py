import time
import threading


is_changed = False


def do_something(lock: threading.Lock) -> None:
    global is_changed
    this_thread = threading.current_thread()
    tname = this_thread.name
    print(f"[{tname}] START", flush=True)

    print(f"[{tname}] first lock acquire attempt ...", flush=True)
    lock.acquire()
    print(f"[{tname}] first lock acquired !", flush=True)

    print(f"[{tname}] second lock acquire attempt ...", flush=True)
    lock.acquire()
    print(f"[{tname}] second lock acquired !", flush=True)

    is_changed = True

    print(f"[{tname}] lock release", flush=True)
    lock.release()

    print(f"[{tname}] STOP", flush=True)


def main() -> None:
    print("[MAIN] START", flush=True)

    lock = threading.Lock()

    print("[MAIN] create thread", flush=True)
    some_thread = threading.Thread(
        target=do_something,
        name="maximus",
        args=(lock,)
    )
    some_thread.daemon = True

    print("[MAIN] start thread", flush=True)
    some_thread.start()

    print("[MAIN] wait 2s ...", flush=True)
    time.sleep(2)

    if is_changed:
        print("[MAIN] second acquire seems to have succeeded")
    else:
        print("[MAIN] second acquire did not succeed")

    print("[MAIN] wait for threads", flush=True)
    some_thread.join(timeout=1.0)

    print("[MAIN] STOP", flush=True)


if __name__ == '__main__':
    main()
