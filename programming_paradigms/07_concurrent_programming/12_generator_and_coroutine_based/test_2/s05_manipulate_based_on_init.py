
import functools
from typing import Generator

hprint = functools.partial(print, '-' * 20)


def do_something(
    should_kek: bool
) -> Generator[None, None, None]:
    print("stage A")
    if should_kek:
        yield
    print("stage B")


def case_1():
    restricted_controller = do_something(True)
    next(restricted_controller)


def case_2():
    unrestricted_controller = do_something(False)
    try:
        next(unrestricted_controller)
    except StopIteration:
        print("StopIteration detected")


def main() -> None:
    case_1()
    hprint()
    case_2()


if __name__ == "__main__":
    main()
