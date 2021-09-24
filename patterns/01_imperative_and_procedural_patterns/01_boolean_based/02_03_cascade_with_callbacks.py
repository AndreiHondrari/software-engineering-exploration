"""
Encapsulated cascade execution.
Side-effects are externalized to a callback.
"""
from typing import Tuple, Callable


def do_cascade(
    stage_1: bool,
    stage_2: bool,
    stage_1_callback: Callable[[], None],
    stage_2_callback: Callable[[], None],
    final_stage_callback: Callable[[], None],
) -> Tuple[bool, bool]:

    if stage_1:
        # stage 1
        stage_1_callback()
        stage_1 = False
    elif stage_2:
        # stage 2
        stage_2_callback()
        stage_2 = False
    else:
        # last stage and reset
        stage_1 = True
        stage_2 = True
        final_stage_callback()

    return stage_1, stage_2


def do_stage_1() -> None:
    print("instruction for stage A")


def do_stage_2() -> None:
    print("instruction for stage B")


def do_final_stage() -> None:
    print("instruction for final stage")


if __name__ == '__main__':

    a = True
    b = True

    a, b = do_cascade(a, b, do_stage_1, do_stage_2, do_final_stage)
    a, b = do_cascade(a, b, do_stage_1, do_stage_2, do_final_stage)
    a, b = do_cascade(a, b, do_stage_1, do_stage_2, do_final_stage)
    a, b = do_cascade(a, b, do_stage_1, do_stage_2, do_final_stage)
    a, b = do_cascade(a, b, do_stage_1, do_stage_2, do_final_stage)
    a, b = do_cascade(a, b, do_stage_1, do_stage_2, do_final_stage)
