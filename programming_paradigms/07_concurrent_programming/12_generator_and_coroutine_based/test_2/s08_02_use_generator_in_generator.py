
import functools
from typing import Generator

hprint = functools.partial(print, '-' * 20)


def do_foo() -> Generator[None, None, None]:
    while True:
        yield
        print("foo")


def do_bar(foo: Generator[None, None, None]) -> Generator[None, None, None]:

    while True:
        next(foo)
        yield


def main() -> None:
    foo = do_foo()
    bar = do_bar(foo)

    for i in range(3):
        next(bar)
        hprint()

    print("-- FIN --")


if __name__ == "__main__":
    main()
