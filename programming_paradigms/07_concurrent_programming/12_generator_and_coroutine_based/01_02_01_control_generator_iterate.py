"""
Control steps of the execution by iterating directly.

Iterating over a generator will run all the generator sections.
"""

import functools
from typing import Generator

hprint = functools.partial(print, '-' * 20)


def do_something() -> Generator[None, None, None]:
    print("SECTION A")
    yield
    print("SECTION B")
    yield
    print("LAST SECTION")


def main() -> None:
    something_controller = do_something()

    for _ in something_controller:
        hprint()

    print(" \n-- END --")


if __name__ == "__main__":
    main()
