"""
Coroutine producer & consumer.

The producer receives the target consumer.
"""
from typing import Generator

VALUES = [1, 3, 5]


def produce(target_generator: Generator[None, int, None]) -> None:
    target_generator.send(None)  # start the target

    # send values to target
    for val in VALUES:
        target_generator.send(val)

    # finalize the target
    target_generator.close()


def consume() -> Generator[None, int, None]:
    while True:
        value = yield  # receive value from producer
        print("value", value)


def main() -> None:
    c: Generator[None, int, None] = consume()
    produce(c)


if __name__ == "__main__":
    main()
