from typing import Callable


def do_something() -> None:
    print("some_instruction")


def give_function() -> Callable[[], None]:
    return do_something


if __name__ == '__main__':
    some_function = give_function()
    some_function()
