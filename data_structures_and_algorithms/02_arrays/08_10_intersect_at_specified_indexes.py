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
    indexes: List[int] = [1, 3, 7, 8]

    SIZE: int = len(l1)
    L2SIZE: int = len(l2)

    assert SIZE == L2SIZE, "Arrays must be equal"

    nice_print(l1, "L1")
    nice_print(l2, "L2")

    l3: List[int] = [k for k in l1]

    for i in indexes:
        l3[i] = l2[i]

    nice_print(l3, "L3")
