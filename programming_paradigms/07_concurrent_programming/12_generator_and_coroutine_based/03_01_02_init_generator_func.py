"""
Generator initialization

Functions can be passed that can be called by the generator.
"""
import functools
from typing import Generator

hprint = functools.partial(print, '-' * 20)


def do_something(
    some_func: callable
) -> Generator[None, None, None]:
    some_func("before")
    yield
    some_func("after")


def my_func(message: str) -> None:
    print("my_func", message)


def main() -> None:
    something_controller = do_something(my_func)

    # first stage
    print("before first call")
    next(something_controller)
    print("after first call")

    hprint()

    # second stage
    print("before second call")

    try:
        next(something_controller)
    except StopIteration:
        print("done")

    print("after second call")

    hprint()

    print(" \n-- END --")


if __name__ == "__main__":
    main()
