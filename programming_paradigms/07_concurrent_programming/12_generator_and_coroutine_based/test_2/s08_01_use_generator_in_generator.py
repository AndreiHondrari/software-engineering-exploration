
import functools
from typing import Generator

hprint = functools.partial(print, '-' * 20)


def do_foo() -> Generator[None, None, None]:
    while True:
        yield
        print("foo")


def do_bar() -> Generator[None, None, None]:
    foo = do_foo()

    while True:
        next(foo)
        yield


def main() -> None:
    bar = do_bar()

    for i in range(3):
        next(bar)
        hprint()

    print("-- FIN --")


if __name__ == "__main__":
    main()
