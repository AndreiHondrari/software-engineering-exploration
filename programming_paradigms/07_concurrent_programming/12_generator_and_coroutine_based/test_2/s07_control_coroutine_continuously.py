
import functools
from typing import Generator

hprint = functools.partial(print, '-' * 20)


def do_something() -> Generator[None, bool, None]:
    while True:
        should = yield
        if should:
            print("section A")
        else:
            print("section B")


def main() -> None:
    some_controller = do_something()
    some_controller.send(None)

    some_controller.send(False)
    some_controller.send(False)
    hprint()
    some_controller.send(True)
    some_controller.send(True)
    hprint()
    some_controller.send(False)
    some_controller.send(False)

    print("-- FIN --")


if __name__ == "__main__":
    main()
