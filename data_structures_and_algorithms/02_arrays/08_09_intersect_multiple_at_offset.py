from typing import List


def nice_print(
    vals: List[int],
    description: str
) -> None:
    representation: str = ", ".join([f"{k: <3}" for k in vals])
    print(f"{description}: [{representation}]")


if __name__ == '__main__':
    l1: List[int] = [11,  22,  33,  44,  55,  66,  77,  88,  99]
    l2: List[int] = [999, 888, 777, 666, 555, 444, 333, 222, 111]
    OFFSET: int = 2
    AMOUNT: int = 3

    SIZE: int = len(l1)
    L2SIZE: int = len(l2)

    assert SIZE == L2SIZE, "Arrays must be equal"

    nice_print(l1, "L1")
    nice_print(l2, "L2")

    l3: List[int] = [k for k in l1]

    for i in range(SIZE):
        if OFFSET <= i < (OFFSET + AMOUNT):
            l3[i] = l2[i]
        else:
            l3[i] = l1[i]

    nice_print(l3, "L3")
