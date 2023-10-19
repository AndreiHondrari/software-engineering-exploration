
import functools
from typing import Generator

hprint = functools.partial(print, '-' * 20)


def do_something() -> Generator[None, int, None]:
    x: int = 0
    while True:
        x = yield x
        x = x * 10


def main() -> None:
    some = do_something()
    next(some)

    for i in range(3):
        print("send", i)
        previous_result = some.send(i)
        print(previous_result)
        hprint()

    print("-- FIN --")


if __name__ == "__main__":
    main()
