from typing import Generator


def do_gen(some: Generator[None, int, None]) -> Generator[int, None, None]:
    some.send(None)  # start

    for i in range(1, 5 + 1):
        yield
        print("AA")

        try:
            some.send(None)
        except StopIteration:
            print("Nothing to do")


def do_coro() -> Generator[None, int, None]:
    for i in range(3):
        yield
        print("ZAAAR")


def main() -> None:
    c: Generator[None, int, None] = do_coro()
    g: Generator[int, None, None] = do_gen(c)

    for i in range(10):
        try:
            next(g)
        except StopIteration:
            print("no more g")


if __name__ == "__main__":
    main()
