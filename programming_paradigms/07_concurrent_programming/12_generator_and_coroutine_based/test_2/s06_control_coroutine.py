
import functools
from typing import Generator

hprint = functools.partial(print, '-' * 20)


def do_something() -> Generator[None, bool, None]:
    should = yield

    if should:
        print("section A")
    else:
        print("section B")


def case_1():
    some_controller = do_something()
    some_controller.send(None)

    try:
        some_controller.send(True)
    except StopIteration:
        print("DONE")


def case_2():
    some_controller = do_something()
    some_controller.send(None)

    try:
        some_controller.send(False)
    except StopIteration:
        print("DONE")


def main() -> None:
    case_1()
    hprint()
    case_2()
    print("-- FIN --")


if __name__ == "__main__":
    main()
