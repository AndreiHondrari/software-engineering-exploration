
import functools
from typing import Generator

hprint = functools.partial(print, '-' * 20)


def do_something(name: str) -> Generator[None, int, None]:
    for i in range(3):
        print(f"do_something [{name}]")
        yield


def main() -> None:
    some1 = do_something("aaa")
    some2 = do_something("bbb")

    while True:
        try:
            next(some1)
            next(some2)
        except StopIteration:
            print("done")
            break

    print("-- FIN --")


if __name__ == "__main__":
    main()
