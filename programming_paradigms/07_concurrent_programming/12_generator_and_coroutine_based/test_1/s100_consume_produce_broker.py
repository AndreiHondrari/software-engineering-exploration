#!python3

import functools

from typing import Generator

hprint = functools.partial(print, "\n#")


def create_events_producer() -> Generator[int, None, None]:
    k = 0

    while True:
        k += 1
        event = 2 * k
        yield event


class StopAccumulator(Exception):
    pass


def create_accumulator() -> Generator[int, int, None]:

    total = 0

    while True:
        try:
            x: int = yield total
        except StopAccumulator:
            yield total

        total += x


def main() -> None:

    events_producer = create_events_producer()
    accumulator = create_accumulator()

    next(accumulator)

    for i in range(10):
        event = next(events_producer)
        accumulator.send(event)

    events_producer.close()

    final: int = accumulator.throw(StopAccumulator)
    print("final total:", final)


if __name__ == "__main__":
    main()
