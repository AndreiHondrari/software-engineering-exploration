

"""
Cascade execution.
Non-encapsulated due to global state -> avoid in favor of encapsulation.
"""

if __name__ == '__main__':

    a = True
    b = True

    def do_cascade() -> None:
        global a, b
        if a:
            # stage 1
            print("instruction for stage A")
            a = False
        elif b:
            # stage 2
            print("instruction for stage B")
            b = False
        else:
            # last stage and reset
            a = True
            b = True
            print("instruction for final stage")

    do_cascade()
    do_cascade()
    do_cascade()
    do_cascade()
    do_cascade()
    do_cascade()
