"""
Control steps of the execution of a generator using `generator.send(None)`

Execute each section from the generator
precisely by issuing it with generator.send(None)

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

    something_controller.send(None)
    hprint()

    something_controller.send(None)
    hprint()

    try:
        something_controller.send(None)
    except StopIteration:
        hprint()
        print("FINISHED")

    print(" \n-- END --")


if __name__ == "__main__":
    main()
