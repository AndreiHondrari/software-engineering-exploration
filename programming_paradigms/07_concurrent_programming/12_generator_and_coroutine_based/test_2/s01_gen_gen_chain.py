from typing import Generator


def do_gen_1() -> Generator[int, None, None]:
    for _ in range(5):
        print('G1 S A')
        yield
        print('G1 S B')


def do_gen_2(some: Generator[int, None, None]) -> Generator[int, None, None]:
    for i in range(10):
        yield
        try:
            next(some)
        except StopIteration:
            print("AR DONE")


def main() -> None:
    g1: Generator[int, None, None] = do_gen_1()
    g2: Generator[int, None, None] = do_gen_2(g1)

    [() for _ in g2]


if __name__ == "__main__":
    main()
