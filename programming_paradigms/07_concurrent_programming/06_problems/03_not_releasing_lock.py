"""
A thread locks and then does not release.
"""
import time
import threading


def tprint(msg: str) -> None:
    this_thread = threading.current_thread()
    print(f"[{this_thread.name}] {msg}", flush=True)


def do_as_victim(
    lock: threading.Lock,
    victim_reached_end: threading.Event
) -> None:
    tprint("START")

    tprint("simulate slow start by waiting 1s ...")
    time.sleep(1)

    tprint("try acquire ...")
    lock.acquire()

    tprint("release lock")
    lock.release()

    victim_reached_end.set()
    tprint("STOP")


def do_offensive_lock(
    lock: threading.Lock
) -> None:
    tprint("START")

    tprint("acquire lock")
    lock.acquire()

    # notice no release of the lock ...
    tprint("STOP")


def main() -> None:
    tprint("START")

    lock = threading.Lock()
    victim_reached_end = threading.Event()

    tprint("create threads")
    victim = threading.Thread(
        target=do_as_victim,
        name="victim",
        args=(lock, victim_reached_end,)
    )
    victim.daemon = True

    perpetrator = threading.Thread(
        target=do_offensive_lock,
        name="perpetrator",
        args=(lock,)
    )
    perpetrator.daemon = True

    tprint("start threads")
    victim.start()
    perpetrator.start()

    tprint("wait for threads to DIE ...")
    victim.join(timeout=2)
    perpetrator.join(timeout=2)

    # check lock
    if lock.locked():
        tprint("lock was never released!")
    else:
        tprint("lock was released!")

    # check victim
    if victim_reached_end.is_set():
        tprint("victim managed to do something!")
    else:
        tprint("victim was offended")

    tprint("STOP")


if __name__ == '__main__':
    main()
