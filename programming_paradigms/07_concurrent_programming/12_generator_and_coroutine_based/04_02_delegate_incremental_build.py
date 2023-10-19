"""
Delegate.

A delegate can be used to do some async operation
and then return the cumulated result of those multiple steps.
"""
import functools
from typing import Generator, List

hprint = functools.partial(print, '-' * 20)


def do_foo() -> Generator[None, None, List[int]]:

    result = []

    for i in range(1, 10):
        yield
        print(f"do step {i}")
        result.append(i * 11)

    return result


def do_bar() -> Generator[None, None, None]:
    foo = do_foo()

    print("before foo")
    hprint()
    result: List[int] = yield from foo
    hprint()
    print("after foo", result)


def main() -> None:
    [() for _ in do_bar()]
    print(" \n-- END --")


if __name__ == "__main__":
    main()
