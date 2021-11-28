"""
Resource depletion.

A thread will take all the resources and not release them for a long time.
"""
import time
import threading


def tprint(msg: str) -> None:
    this_thread = threading.current_thread()
    print(f"[{this_thread.name}] {msg}", flush=True)


def do_slow_achieve(
    semaphore: threading.Semaphore,
    acquired_resource_event: threading.Event
) -> None:
    tprint("START")

    tprint("be slow -> wait for 1s ...")
    time.sleep(1)

    tprint("try to acquire any resources")
    semaphore.acquire()
    acquired_resource_event.set()

    tprint("acquired, now do something")
    time.sleep(1)

    semaphore.release()

    tprint("STOP")


def do_greedy(
    semaphore: threading.Semaphore,
) -> None:
    tprint("START")

    tprint("acquire EVERYTHING")
    acquire_count = 0
    while True:
        result = semaphore.acquire(blocking=False)
        if result:
            acquire_count += 1
        else:
            break

    tprint("do something with them for a long time ...")
    time.sleep(100)

    semaphore.release(n=acquire_count)

    tprint("STOP")


def main() -> None:
    tprint("START")

    semaphore = threading.Semaphore(value=3)
    slow_threads_acquired_resource = threading.Event()

    tprint("create threads")
    slow_thread_1 = threading.Thread(
        target=do_slow_achieve,
        name="slime",
        args=(semaphore, slow_threads_acquired_resource,)
    )
    slow_thread_1.daemon = True

    slow_thread_2 = threading.Thread(
        target=do_slow_achieve,
        name="slug",
        args=(semaphore, slow_threads_acquired_resource,)
    )
    slow_thread_2.daemon = True

    greedy_thread = threading.Thread(
        target=do_greedy,
        name="GRINCH",
        args=(semaphore,)
    )
    greedy_thread.daemon = True

    tprint("start treads")
    slow_thread_1.start()
    slow_thread_2.start()
    greedy_thread.start()

    tprint("wait for threads to DIE ...")
    MAX_TIMEOUT = 2
    slow_thread_1.join(timeout=MAX_TIMEOUT)
    slow_thread_2.join(timeout=MAX_TIMEOUT)
    greedy_thread.join(timeout=MAX_TIMEOUT)

    if slow_threads_acquired_resource.is_set():
        tprint("one of the slow threads made it \\:D/ !")
    else:
        tprint("NONE of the slow threads made it :( !")

    tprint("STOP")


if __name__ == '__main__':
    main()
