
import functools
from typing import Generator

hprint = functools.partial(print, '-' * 20)


def do_foo(other: Generator[int, None, None]) -> Generator[None, None, None]:
    while True:
        yield
        x = next(other)
        print("foo", x)


def do_bar(other: Generator[int, None, None]) -> Generator[int, None, None]:

    while True:
        x = next(other)
        print("bar", x)
        yield x


def do_kek() -> Generator[int, None, None]:

    i = 0
    while True:
        print("kek", i)
        yield i
        i += 1


def main() -> None:
    kek = do_kek()

    bar = do_bar(kek)

    foo = do_foo(bar)
    next(foo)  # only coro needs start

    for _ in range(3):
        foo.send(None)  # control all of them through one next
        hprint()

    print("-- FIN --")


if __name__ == "__main__":
    main()
