"""
Cascade execution with closure callbacks.
"""

from typing import Callable, Tuple, Any


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


def do_stage(version: str) -> None:
    print(f"[{version}] instruction for stage")


def create_closure(
    version: str,
    func: Callable[..., Any]
) -> Callable[[], None]:

    def inner() -> None:
        func(version)

    return inner


if __name__ == '__main__':

    do_stage_v1 = create_closure("v1", do_stage)
    do_stage_v2 = create_closure("v2", do_stage)

    print("Section 1")
    a = True
    b = True
    a, b = do_cascade(a, b, do_stage_v1, do_stage_v2)
    a, b = do_cascade(a, b, do_stage_v1, do_stage_v2)
    a, b = do_cascade(a, b, do_stage_v1, do_stage_v2)

    print("\nSection 2")
    a = True
    b = True
    a, b = do_cascade(a, b, do_stage_v2, do_stage_v1)
    a, b = do_cascade(a, b, do_stage_v2, do_stage_v1)
    a, b = do_cascade(a, b, do_stage_v2, do_stage_v1)
