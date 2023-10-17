"""
Control steps of the execution by iterating with `generator.send()`.

It is possible to call generator.send(None) in a loop.
Has similar effect as iterating directly over the generator.

Reason to use: allows for finer control inside a loop.
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

    while True:
        try:
            something_controller.send(None)
            hprint()
        except StopIteration:
            hprint()
            print("FINISHED")
            break

    print(" \n-- END --")


if __name__ == "__main__":
    main()
