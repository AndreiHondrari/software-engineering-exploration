
import functools
from typing import Generator

hprint = functools.partial(print, '-' * 20)


def do_foo() -> Generator[None, None, None]:
    while True:
        yield
        print("foo")


def do_bar(other: Generator[None, None, None]) -> Generator[None, None, None]:

    while True:
        yield
        next(other)
        print("bar")


def do_kek(other: Generator[None, None, None]) -> Generator[None, None, None]:

    while True:
        yield
        next(other)
        print("kek")


def main() -> None:
    foo = do_foo()
    next(foo)  # start foo

    bar = do_bar(foo)
    next(bar)  # start bar

    kek = do_kek(bar)
    next(kek)

    for i in range(3):
        print("step", i)
        next(kek)  # control all of them through one next
        hprint()

    print("-- FIN --")


if __name__ == "__main__":
    main()
