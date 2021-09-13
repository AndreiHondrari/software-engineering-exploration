from typing import Callable


def loop_callee(
    limit: int,
    callback: Callable[[], None],
    i: int = 0
) -> None:
    if i >= limit:  # this will break the loop
        return

    callback()
    loop_callee(limit, callback, i=i+1)


def do_this() -> None:
    print("instruction_1")
    print("instruction_2")


def do_that() -> None:
    print("instruction_x")
    print("instruction_y")


if __name__ == '__main__':
    print("Call this sequence")
    loop_callee(3, do_this)

    print("\nCall that sequence")
    loop_callee(2, do_that)
