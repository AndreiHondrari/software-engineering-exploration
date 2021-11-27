"""
The point here is that one thread waits for the other and viceverse,
waiting for ever, effectively being in a state of deadlock.
"""
import threading


def do_this(
    condition_a: threading.Condition,
    condition_b: threading.Condition,
    reached_event: threading.Event,
) -> None:
    this_thread = threading.current_thread()
    tname = this_thread.name
    print(f"[{tname}] START", flush=True)

    print(f"[{tname}] wait for A", flush=True)
    with condition_a:
        condition_a.wait()
    print(f"[{tname}] A passed", flush=True)

    condition_b.notify()

    reached_event.set()

    print(f"[{tname}] STOP", flush=True)


def do_that(
    condition_a: threading.Condition,
    condition_b: threading.Condition,
    reached_event: threading.Event,
) -> None:
    this_thread = threading.current_thread()
    tname = this_thread.name
    print(f"[{tname}] START", flush=True)

    print(f"[{tname}] wait for B", flush=True)
    with condition_b:
        condition_b.wait()
    print(f"[{tname}] B passed", flush=True)

    condition_a.notify()

    reached_event.set()

    print(f"[{tname}] STOP", flush=True)


def main() -> None:
    print("[MAIN] START", flush=True)

    condition_a = threading.Condition()
    condition_b = threading.Condition()

    reached_event = threading.Event()

    print("[MAIN] create threads", flush=True)
    thread_x = threading.Thread(
        target=do_this,
        name="THIS_THREAD",
        args=(condition_a, condition_b, reached_event,)
    )
    thread_x.daemon = True

    thread_y = threading.Thread(
        target=do_that,
        name="THAT_THREAD",
        args=(condition_a, condition_b, reached_event,)
    )
    thread_y.daemon = True

    print("[MAIN] start threads", flush=True)
    thread_x.start()
    thread_y.start()

    print("[MAIN] wait for threads", flush=True)
    thread_x.join(timeout=1)
    thread_y.join(timeout=1)

    if reached_event.is_set():
        print("[MAIN] one of the threads made it \\:D/ !", flush=True)
    else:
        print("[MAIN] NONE of the threads made it :( !", flush=True)

    print("[MAIN] STOP", flush=True)


if __name__ == '__main__':
    main()
