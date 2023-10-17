"""
Control steps of the execution of a generator using `next(generator)`

Execute each section from the generator
precisely by issuing it with next(generator)

Last section (after the last yield) will always raise a StopIteration.
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

    next(something_controller)
    hprint()

    next(something_controller)
    hprint()

    try:
        next(something_controller)
    except StopIteration:
        hprint()
        print("FINISHED")

    print(" \n-- END --")


if __name__ == "__main__":
    main()
