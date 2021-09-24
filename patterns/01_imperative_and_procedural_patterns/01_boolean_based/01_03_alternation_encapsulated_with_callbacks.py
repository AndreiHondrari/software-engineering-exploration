"""
Encapsulated alternation
Side-effects are externalized to a callback.
"""
from typing import Callable, Any


def do_alternation(
    condition: bool,
    direct_callback: Callable[..., Any],
    alternative_callback: Callable[..., Any]
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


def do_this() -> None:
    print("THIS")


def do_that() -> None:
    print("THAT")


if __name__ == '__main__':

    a = True

    a = do_alternation(a, do_this, do_that)
    a = do_alternation(a, do_this, do_that)
    a = do_alternation(a, do_this, do_that)
    a = do_alternation(a, do_this, do_that)
