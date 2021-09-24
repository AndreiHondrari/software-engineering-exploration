"""
Cascade execution. Encapsulated.
Has side-effects (the print).
"""
from typing import Tuple


def do_cascade(
    stage_1: bool,
    stage_2: bool,
) -> Tuple[bool, bool]:

    if stage_1:
        # stage 1
        print("instruction for stage A")
        stage_1 = False
    elif stage_2:
        # stage 2
        print("instruction for stage B")
        stage_2 = False
    else:
        # last stage and reset
        stage_1 = True
        stage_2 = True
        print("instruction for final stage")

    return stage_1, stage_2


if __name__ == '__main__':

    a = True
    b = True

    a, b = do_cascade(a, b)
    a, b = do_cascade(a, b)
    a, b = do_cascade(a, b)
    a, b = do_cascade(a, b)
    a, b = do_cascade(a, b)
    a, b = do_cascade(a, b)
