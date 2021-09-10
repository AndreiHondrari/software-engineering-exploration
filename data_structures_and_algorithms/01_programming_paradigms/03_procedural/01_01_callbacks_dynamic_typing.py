from typing import Callable


def do_something(
    some_function: Callable[[], None]
) -> None:
    print("pre")  # pre operation
    some_function()  # infix operation / callback call
    print("post")  # post operation


def do_this() -> None:
    print("instruction_1")
    print("instruction_2")


def do_that() -> None:
    print("instruction_x")
    print("instruction_y")


if __name__ == '__main__':
    print("Call this")
    do_something(do_this)

    print("\nCall that")
    do_something(do_that)
