"""
Generator producer & consumer.

The consumer receives the source producer.
"""
from typing import Generator, List

VALUES: List[int] = [1, 3, 5]


def produce() -> Generator[int, None, None]:
    for value in VALUES:
        yield value


def consume(source_generator: Generator[int, None, None]) -> None:
    for value in source_generator:  # extract value from producer
        print("value", value)


def main() -> None:
    p: Generator[int, None, None] = produce()
    consume(p)


if __name__ == "__main__":
    main()
