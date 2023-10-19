"""
Delegate.

It is possible to pass the control to a delegated generator.
Once the delegate finishes, it can return to the delegator a result.
"""
import functools
from typing import Generator

hprint = functools.partial(print, '-' * 20)


def do_foo() -> Generator[None, None, str]:
    print("stage A")
    yield
    print("stage B")
    yield
    print("stage C")
    yield
    print("last stage")

    return "SOMETHING"


def do_bar() -> Generator[None, None, None]:
    foo = do_foo()

    print("before foo")
    hprint()
    result: str = yield from foo
    hprint()
    print("after foo", result)


def main() -> None:
    [() for _ in do_bar()]
    print(" \n-- END --")


if __name__ == "__main__":
    main()
