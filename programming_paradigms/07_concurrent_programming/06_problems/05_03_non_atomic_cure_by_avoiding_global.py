"""
In order to protect against undetermined behaviour while using
non-atomic operators, one could avoid global state alltogether.
"""

import threading
import ctypes
import multiprocessing as mp


def do_inc(
    value: mp.Value,
    target: int
) -> None:

    for _ in range(target):
        with value.get_lock():
            value.value += 1


def main() -> None:
    NO_OF_THREADS = 10
    TARGET = 100_000

    k = mp.Value(ctypes.c_int)

    print("create threads")
    threads = [
        threading.Thread(target=do_inc, args=(k, TARGET,))
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
    result = k.value == EXPECTED
    print(f"CHECK {k.value} == {EXPECTED} ? : {result}")


if __name__ == '__main__':
    main()
