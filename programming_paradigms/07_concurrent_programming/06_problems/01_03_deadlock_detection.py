"""
Detect deadlock and force continue
"""
import time
import threading


def tprint(msg: str) -> None:
    this_thread = threading.current_thread()
    print(f"[{this_thread.name}] {msg}", flush=True)


def do_this(
    signal_a: threading.Event,
    signal_b: threading.Event,
    condition_a: threading.Condition,
    condition_b: threading.Condition,
    reached_event: threading.Event,
) -> None:
    tprint("START")

    tprint("signal B")
    signal_b.set()

    tprint("simulate delay after signal")
    time.sleep(1)

    tprint("evaluate barrier signal A")
    if signal_a.is_set():
        tprint("barrier signal A detected, waiting ...")
        with condition_a:
            condition_a.wait()

        tprint("passed barrier A")

    else:
        tprint("no barrier signal A detected")

    tprint("release B")
    with condition_b:
        condition_b.notify_all()

    reached_event.set()

    tprint("STOP")


def do_that(
    signal_a: threading.Event,
    signal_b: threading.Event,
    condition_a: threading.Condition,
    condition_b: threading.Condition,
    reached_event: threading.Event,
) -> None:
    tprint("START")

    tprint("signal A")
    signal_a.set()

    tprint("simulate delay after signal")
    time.sleep(1)

    tprint("evaluate barrier signal B")
    if signal_b.is_set():
        tprint("barrier signal B detected, waiting ...")
        with condition_b:
            condition_b.wait()
        tprint("passed barrier B")
    else:
        tprint("no barrier signal B detected")

    tprint("release A")
    with condition_a:
        condition_a.notify_all()

    reached_event.set()

    tprint("STOP")


def detect_deadlock(
    signal_a: threading.Event,
    signal_b: threading.Event,
    condition_a: threading.Condition,
    reached_event: threading.Event,
) -> None:
    tprint("START")

    tprint("POLL")
    while not reached_event.is_set():

        if signal_a.is_set() and signal_b.is_set():
            tprint("both lock signals activ. Wait for deadlock detection ...")
            time.sleep(1)

            if not reached_event.is_set():
                tprint("DEADLOCK DETECTED. Release barrier A")
                with condition_a:
                    condition_a.notify()
                tprint("barrier released for A")

    tprint("STOP")


def main() -> None:
    tprint("START")

    signal_a = threading.Event()
    signal_b = threading.Event()

    condition_a = threading.Condition()
    condition_b = threading.Condition()

    reached_event = threading.Event()

    tprint("create threads")
    thread_x = threading.Thread(
        target=do_this,
        name="maximus",
        args=(signal_a, signal_b, condition_a, condition_b, reached_event,)
    )
    thread_x.daemon = True

    thread_y = threading.Thread(
        target=do_that,
        name="GANDALF",
        args=(signal_a, signal_b, condition_a, condition_b, reached_event,)
    )
    thread_y.daemon = True

    deadlock_detective = threading.Thread(
        target=detect_deadlock,
        name="detective",
        args=(signal_a, signal_b, condition_a, reached_event,)
    )
    deadlock_detective.daemon = True

    tprint("start treads")
    thread_x.start()
    thread_y.start()
    deadlock_detective.start()

    tprint("wait for threads to DIE ...")

    MAX_TIMEOUT = 3
    thread_x.join(timeout=MAX_TIMEOUT)
    thread_y.join(timeout=MAX_TIMEOUT)
    deadlock_detective.join(timeout=MAX_TIMEOUT)

    if reached_event.is_set():
        tprint("one of the threads made it \\:D/ !")
    else:
        tprint("NONE of the threads made it :( !")

    tprint("STOP")


if __name__ == '__main__':
    main()
