from typing import Callable


def do_this() -> None:
    print("instruction_1")
    print("instruction_2")


def do_that() -> None:
    print("instruction_x")
    print("instruction_y")


def wrap(wrapee: Callable[[], None]) -> Callable[[], None]:

    def inner() -> None:
        print("pre_instruction")
        wrapee()
        print("post_instruction")

    return inner


if __name__ == '__main__':
    do_proxied_this = wrap(do_this)
    do_proxied_that = wrap(do_that)

    print("Call this")
    do_proxied_this()

    print("\nCall that")
    do_proxied_that()
