"""
Data Race

One might think that because of the Global Interpreter Lock in Python
there will be no consequences in terms of races, rendering the execution of
a multi-threaded program in Python as deterministic, when in fact,
due to the nature of some operations which are in fact spread over several
low-level VM operations, we end up with a non-deterministic output.

For example:

Addding to a global variable 200_000 times over 4 threads should yield a
total of 800_000, when in fact this number is lower and random due to a race
that occurs between the threads when adding in several steps.

Reason:

The function definition:

def f1():
       global x
       x = x + 1

Results in the following disassembly:

dis.dis(f1)
        0 LOAD_GLOBAL              0 (x)
        2 LOAD_CONST               1 (1)
        4 BINARY_ADD
        6 STORE_GLOBAL             0 (x)
        8 LOAD_CONST               0 (None)
        10 RETURN_VALUE

Between LOAD_GLOBAL and STORE_GLOBAL, several steps happen, and
two threads might be loading the same value and adding to it.

"""

import threading
from typing import List

x: int = 0

ITERATIONS_PER_THREAD = 200_000


def do_some() -> None:
    global x

    for i in range(ITERATIONS_PER_THREAD):
        x = x + 1


def main() -> None:

    # declare threads
    NO_OF_THREADS = 4

    threads: List[threading.Thread] = [
        threading.Thread(target=do_some)
        for _ in range(NO_OF_THREADS)
    ]

    # start all threads
    for t in threads:
        t.start()

    # wait for threads to finish
    for t in threads:
        t.join()

    print("Expected X:", NO_OF_THREADS * ITERATIONS_PER_THREAD)
    print("FINAL X:", x)


if __name__ == "__main__":
    main()
