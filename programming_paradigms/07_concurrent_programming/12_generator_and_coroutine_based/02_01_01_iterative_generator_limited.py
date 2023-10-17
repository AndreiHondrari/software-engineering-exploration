"""
Generator containing limited loop

A generator that yields in a limited loop can
repeat a series of PRE/MID/POST operations a specific number of times.

It makes sense to use this for cases where:
- you want to start with pre stage
- end with post stage
- play post->pre in between
"""

import functools
from typing import Generator

hprint = functools.partial(print, '-' * 20)


def do_something() -> Generator[None, None, None]:
    for i in range(3):
        print(f"{i} stage A")
        yield
        print(f"{i} stage B")


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
