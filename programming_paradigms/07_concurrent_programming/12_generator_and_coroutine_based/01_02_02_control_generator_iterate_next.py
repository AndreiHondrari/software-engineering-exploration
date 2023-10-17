"""
Control steps of the execution by iterating with `next(generator)`.

It is possible to call next on the generator in a loop.
Has similar effect as iterating directly over the generator.

Reason to use: allows for finer control inside a loop.
"""

import functools
from typing import Generator

hprint = functools.partial(print, '-' * 20)


def do_something() -> Generator[None, None, None]:
    print("SECTION A")
    yield
    print("SECTION B")
    yield
    print("LAST SECTION")


def main() -> None:
    something_controller = do_something()

    while True:
        try:
            next(something_controller)
            hprint()
        except StopIteration:
            hprint()
            print("FINISHED")
            break

    print(" \n-- END --")


if __name__ == "__main__":
    main()
