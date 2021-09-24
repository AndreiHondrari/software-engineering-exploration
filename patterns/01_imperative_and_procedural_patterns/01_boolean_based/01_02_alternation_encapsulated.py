"""
Encapsulated alternation
Has side-effects (print)
"""


def do_alternation(condition: bool) -> bool:
    """
    Does something according to condition and then returnes the oposite
    value of the condition.
    """

    if condition:
        print("this")
    else:
        print("that")
    return not condition


if __name__ == '__main__':

    a = True

    a = do_alternation(a)
    a = do_alternation(a)
    a = do_alternation(a)
    a = do_alternation(a)
