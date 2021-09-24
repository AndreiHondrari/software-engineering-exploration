"""
Alternation with closure callbacks.
"""
from typing import Callable, Any


def do_alternation(
    condition: bool,
    direct_callback: Callable[[], None],
    alternative_callback: Callable[[], None]
) -> bool:
    """
    Does something according to condition and then returnes the oposite
    value of the condition.
    """

    if condition:
        direct_callback()
    else:
        alternative_callback()
    return not condition


def do_this(version: str) -> None:
    print(f"[{version}] THIS")


def do_that(version: str) -> None:
    print(f"[{version}] THAT")


def create_closure(
    version: str,
    func: Callable[..., Any]
) -> Callable[[], None]:
    def inner() -> None:
        func(version)
    return inner


if __name__ == '__main__':

    a = True

    do_this_v1 = create_closure("v1", do_this)
    do_this_v2 = create_closure("v2", do_this)
    do_that_v1 = create_closure("v1", do_that)
    do_that_v2 = create_closure("v2", do_that)

    print("Section 1")
    a = do_alternation(a, do_this_v1, do_that_v1)
    a = do_alternation(a, do_this_v1, do_that_v1)

    print("\nSection 2")
    a = do_alternation(a, do_this_v2, do_that_v2)
    a = do_alternation(a, do_this_v2, do_that_v2)

    print("\nSection 3")
    a = do_alternation(a, do_this_v1, do_that_v2)
    a = do_alternation(a, do_this_v1, do_that_v2)
