
import functools
from typing import Generator

hprint = functools.partial(print, '-' * 20)


def do_foo() -> Generator[None, None, None]:
    print("foo start")

    while True:
        yield
        print("foo")


def do_bar(foo: Generator[None, None, None]) -> Generator[None, None, None]:
    print("bar start")

    while True:
        yield
        next(foo)


def main() -> None:
    foo = do_foo()
    next(foo)  # start generator

    bar = do_bar(foo)
    bar.send(None)  # start coroutine

    hprint()

    for i in range(3):
        print("step", i)
        bar.send(None)
        hprint()

    print("-- FIN --")


if __name__ == "__main__":
    main()
