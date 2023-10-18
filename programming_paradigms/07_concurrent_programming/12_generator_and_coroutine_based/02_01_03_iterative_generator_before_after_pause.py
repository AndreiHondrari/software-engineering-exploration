"""
Generator with inner loop.

Placing an operation before or after the yield (pause)
has some implications.

Placing it after the yield requires starting the generator before using it.
Placing it before the yield does not require any pre-start.
"""
import functools
from typing import Generator

hprint = functools.partial(print, '-' * 20)


def do_foo() -> Generator[None, None, None]:
    """
    Pre-yield placement.
    Can be used immediately.
    """
    while True:
        print("do_foo")
        yield


def do_bar() -> Generator[None, None, None]:
    """
    Post-yield placement.
    Requires a start (so it can reach the yield).
    """
    while True:
        yield
        print("do_bar")


def main() -> None:
    foo: Generator[None, None, None] = do_foo()

    bar: Generator[None, None, None] = do_bar()
    next(bar)  # needs start

    for i in range(3):
        print("step", i)
        next(foo)
        next(bar)
        hprint()

    print("-- FIN --")


if __name__ == "__main__":
    main()
