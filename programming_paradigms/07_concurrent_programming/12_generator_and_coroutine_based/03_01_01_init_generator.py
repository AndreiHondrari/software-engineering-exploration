"""
Generator initialization

Use values passed to generator.
Multiple values can be used distinctevily
in separate sections.
"""

import functools
from typing import Generator

hprint = functools.partial(print, '-' * 20)


def do_something(
    message_1: str,
    message_2: str
) -> Generator[None, None, None]:
    print(message_1)
    yield
    print(message_2)


def main() -> None:
    something_controller = do_something("foo", "bar")

    [() for _ in something_controller]

    print(" \n-- END --")


if __name__ == "__main__":
    main()
