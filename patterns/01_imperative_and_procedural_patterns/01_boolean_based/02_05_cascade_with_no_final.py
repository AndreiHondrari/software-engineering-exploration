"""
Encapsulated cascade execution with no final.
"""
from typing import Tuple, Callable


def do_cascade(
    stage_1: bool,
    stage_2: bool,
    stage_1_callback: Callable[[], None],
    stage_2_callback: Callable[[], None],
) -> Tuple[bool, bool]:

    if stage_1:
        # stage 1
        stage_1_callback()
        stage_1 = False
    elif stage_2:
        # stage 2
        stage_2_callback()
        stage_2 = False

    return stage_1, stage_2


def do_stage_1() -> None:
    print("instruction for stage A")


def do_stage_2() -> None:
    print("instruction for stage B")


if __name__ == '__main__':

    a = True
    b = True

    a, b = do_cascade(a, b, do_stage_1, do_stage_2)
    a, b = do_cascade(a, b, do_stage_1, do_stage_2)

    # nothing happens after this point
    a, b = do_cascade(a, b, do_stage_1, do_stage_2)
    a, b = do_cascade(a, b, do_stage_1, do_stage_2)
