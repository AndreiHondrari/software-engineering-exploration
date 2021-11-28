"""
Deadlock with events and conditions.
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

    tprint("start treads")
    thread_x.start()
    thread_y.start()

    tprint("wait for threads to DIE ...")
    thread_x.join(timeout=2)
    thread_y.join(timeout=2)

    if reached_event.is_set():
        tprint("one of the threads made it \\:D/ !")
    else:
        tprint("NONE of the threads made it :( !")

    tprint("STOP")


if __name__ == '__main__':
    main()
