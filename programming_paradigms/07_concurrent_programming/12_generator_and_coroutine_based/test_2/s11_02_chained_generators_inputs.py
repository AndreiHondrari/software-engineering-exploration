
import functools
from typing import Generator

hprint = functools.partial(print, '-' * 20)


def do_foo() -> Generator[None, int, None]:
    while True:
        x: int = yield
        print("foo", x)


def do_bar(other: Generator[None, int, None]) -> Generator[None, int, None]:

    while True:
        x: int = yield
        other.send(x)
        print("bar", x)


def do_kek(other: Generator[None, int, None]) -> Generator[None, int, None]:

    while True:
        x: int = yield
        other.send(x)
        print("kek", x)


def main() -> None:
    foo = do_foo()
    next(foo)  # start foo

    bar = do_bar(foo)
    next(bar)  # start bar

    kek = do_kek(bar)
    next(kek)

    for i in range(3):
        kek.send(i)  # control all of them through one next
        hprint()

    print("-- FIN --")


if __name__ == "__main__":
    main()
