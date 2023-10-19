
import functools
from typing import Generator

hprint = functools.partial(print, '-' * 20)


def do_something() -> Generator[None, int, None]:
    while True:
        x: int = yield
        print("foo", x)


def main() -> None:
    some = do_something()
    next(some)

    for i in range(3):
        some.send(i)
        hprint()

    print("-- FIN --")


if __name__ == "__main__":
    main()
