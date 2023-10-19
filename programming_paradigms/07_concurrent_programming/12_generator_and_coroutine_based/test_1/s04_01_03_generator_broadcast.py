"""
Generator broadcasting
"""
from typing import Generator

VALUES = [1, 3, 5]


def broadcast() -> Generator[int, None, None]:

    # broadcast to targets
    for value in VALUES:
        yield value


def consume(
    message: str,
    source_publisher: Generator[int, None, None]
):
    for value in source_publisher:
        print(f"[{message}] value", value)


def main() -> None:
    b = broadcast()

    for value in b:

        consume('aaa', b)
        consume('bbb', b)


if __name__ == "__main__":
    main()
