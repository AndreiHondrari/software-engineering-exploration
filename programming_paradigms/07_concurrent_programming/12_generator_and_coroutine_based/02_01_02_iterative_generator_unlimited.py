"""
Generator containing unlimited loop

A generator that yields in a unlimited loop can
repeat a series of PRE/MID/POST operations until the caller
no longer needs new operations to be executed.

MID = POST + PRE

Useful for:
- continuous repetition of code segments
"""

import functools
from typing import Generator

hprint = functools.partial(print, '-' * 20)


def do_something() -> Generator[None, None, None]:
    i = 0
    while True:
        print(f"{i} do some")
        yield
        i += 1


def main() -> None:
    something_controller = do_something()

    for i in range(10):
        print(f"step {i}")
        try:
            next(something_controller)
        except StopIteration:
            hprint()
            print("DONE")
            break

        hprint()

    print(" \n-- END --")


if __name__ == "__main__":
    main()
