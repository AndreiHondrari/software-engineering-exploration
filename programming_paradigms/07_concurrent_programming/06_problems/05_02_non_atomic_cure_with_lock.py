"""
In order to protect against undetermined behaviour while using
non-atomic operators on global state, one must use a lock while performing the
non-atomic operation.
"""

import threading

k = 0

NO_OF_THREADS = 10


def do_inc(
    lock: threading.Lock,
    target: int
) -> None:
    global k

    for _ in range(target):
        lock.acquire()
        k += 1
        lock.release()


def main() -> None:
    global k

    TARGET = 1_000_000

    print("create threads")
    lock = threading.Lock()
    threads = [
        threading.Thread(target=do_inc, args=(lock, TARGET,))
        for _ in range(NO_OF_THREADS)
    ]

    print("start threads")
    for t in threads:
        t.start()

    print("wait for threads to DIE ...")
    for t in threads:
        t.join()

    # check results
    EXPECTED = NO_OF_THREADS * TARGET
    result = k == EXPECTED
    print(f"CHECK {k} == {EXPECTED} ? : {result}")


if __name__ == '__main__':
    main()
