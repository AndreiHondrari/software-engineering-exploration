from typing import Callable


def create_function() -> Callable[[], None]:
    def inner() -> None:
        print("some_instruction")
    return inner


if __name__ == '__main__':
    my_function = create_function()
    my_function()
