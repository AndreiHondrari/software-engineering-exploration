"""

"""
from typing import Generator, List

VALUES = [1, 3, 5]


def broadcast(
    target_consumers: List[Generator[None, int, None]]
):
    # start targets
    for target_consumer in target_consumers:
        target_consumer.send(None)

    # broadcast to targets
    for val in VALUES:
        for target_consumer in target_consumers:
            target_consumer.send(val)

    # finalize target consumers
    for target_consumer in target_consumers:
        target_consumer.close()


def consume(message) -> Generator[None, int, None]:
    while True:
        value = yield
        print(f"[{message}] value", value)


def main() -> None:
    broadcast([consume('aaa'), consume('bbb')])


if __name__ == "__main__":
    main()
