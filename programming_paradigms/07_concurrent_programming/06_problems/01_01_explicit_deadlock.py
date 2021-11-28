"""
The point here is that one thread waits for the other and viceverse,
waiting for ever, effectively being in a state of deadlock.
"""
import time
import threading

reached_end: bool = False
lock_a: bool = False
lock_b: bool = False


def do_this() -> None:
    global lock_a
    global lock_b
    global reached_end

    this_thread = threading.current_thread()
    tname = this_thread.name
    print(f"[{tname}] START", flush=True)

    print(f"[{tname}] lock B", flush=True)
    lock_b = True

    print(f"[{tname}] simulate slow wait after lock", flush=True)
    time.sleep(1)

    print(f"[{tname}] wait for A", flush=True)
    while lock_a:
        time.sleep(0.1)

    print(f"[{tname}] release lock B", flush=True)
    lock_b = False

    reached_end = True

    print(f"[{tname}] STOP", flush=True)


def do_that() -> None:
    global lock_a
    global lock_b
    global reached_end

    this_thread = threading.current_thread()
    tname = this_thread.name
    print(f"[{tname}] START", flush=True)

    print(f"[{tname}] lock A", flush=True)
    lock_a = True

    print(f"[{tname}] simulate slow wait after lock", flush=True)
    time.sleep(1)

    print(f"[{tname}] wait for B", flush=True)
    while lock_b:
        time.sleep(0.1)

    print(f"[{tname}] release A", flush=True)
    lock_a = False

    reached_end = True

    print(f"[{tname}] STOP", flush=True)


def main() -> None:
    print("[MAIN] START", flush=True)

    print("[MAIN] create threads", flush=True)
    thread_x = threading.Thread(
        target=do_this,
        name="THIS_THREAD",
    )
    thread_x.daemon = True

    thread_y = threading.Thread(
        target=do_that,
        name="THAT_THREAD",
    )
    thread_y.daemon = True

    print("[MAIN] start threads", flush=True)
    thread_x.start()
    thread_y.start()

    print("[MAIN] wait for threads", flush=True)
    thread_x.join(timeout=2)
    thread_y.join(timeout=2)

    if reached_end:
        print("[MAIN] one of the threads made it \\:D/ !", flush=True)
    else:
        print("[MAIN] NONE of the threads made it :( !", flush=True)

    print("[MAIN] STOP", flush=True)


if __name__ == '__main__':
    main()
