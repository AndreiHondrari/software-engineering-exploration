"""
Non-encapsulated alternation. Avoid!
While this works, there is a global state being used which violates
the criteria for decomposition promoted by David Parnas.
"""

if __name__ == '__main__':

    a = True

    def do_alternation() -> None:
        global a
        if a:
            print("this")
        else:
            print("that")
        a = not a

    do_alternation()
    do_alternation()
    do_alternation()
    do_alternation()
