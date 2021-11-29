"""
Some operations might seem atomic but they are not in fact.

Example:

x += 1

which actually occurs in several steps

* acquire x
* add value to x
* store the value to x

"""

import threading

k = 0

NO_OF_THREADS = 10


def do_inc(target: int) -> None:
    global k

    for _ in range(target):
        k += 1


def launch_incrementation(target: int) -> None:
    global k
    k = 0
    threads = [
        threading.Thread(target=do_inc, args=(target,))
        for _ in range(NO_OF_THREADS)
    ]

    print("start threads")
    for t in threads:
        t.start()

    print("wait for threads to DIE ...")
    for t in threads:
        t.join()


def main() -> None:

    print("check small target")
    SMALL_TARGET = 100
    launch_incrementation(SMALL_TARGET)

    SMALL_EXPECTED = NO_OF_THREADS * SMALL_TARGET
    result = k == SMALL_EXPECTED
    print(f"SMALL {k} == {SMALL_EXPECTED} ? : {result}")

    print("\ncheck large target")
    LARGE_TARGET = 1_000_000
    launch_incrementation(LARGE_TARGET)

    LARGE_EXPECTED = NO_OF_THREADS * LARGE_TARGET
    result = k == LARGE_EXPECTED
    print(f"LARGE {k} == {LARGE_EXPECTED} ? : {result}")


if __name__ == '__main__':
    main()
