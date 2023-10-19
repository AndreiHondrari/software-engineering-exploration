
import functools
from typing import Generator

hprint = functools.partial(print, '-' * 20)


def do_foo():
    while True:
        print("do_foo")
        yield


def do_bar():
    while True:
        yield
        print("do_bar")


def main() -> None:
    foo = do_foo()

    bar = do_bar()
    next(bar)  # needs start

    for i in range(3):
        print("step", i)
        next(foo)
        next(bar)
        hprint()

    print("-- FIN --")


if __name__ == "__main__":
    main()
