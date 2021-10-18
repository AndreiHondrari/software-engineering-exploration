from typing import List
from random import random


if __name__ == '__main__':
    l1: List[int] = [11,  22,  33,  44,  55,  66,  77,  88,  99]

    print(f"L1 BEFORE: {l1}")

    available_indexes = [k for k in range(len(l1))]
    indexes_amount: int = len(available_indexes)

    pos1: int
    pos2: int
    first: int
    second: int

    while len(available_indexes) > 0:
        # pop first
        size = len(available_indexes)
        pos1 = int(random() * size)
        first = available_indexes[pos1]
        available_indexes = (
            available_indexes[:pos1] + available_indexes[pos1+1:]
        )
        size -= 1

        if size == 0:
            break

        # pop second
        pos2 = int(random() * size)
        second = available_indexes[pos2]
        available_indexes = (
            available_indexes[:pos2] + available_indexes[pos2+1:]
        )

        # swap
        # xor swap because we're cool
        l1[first] = l1[first] ^ l1[second]
        l1[second] = l1[first] ^ l1[second]
        l1[first] = l1[first] ^ l1[second]

    print(f"L1 AFTER:  {l1}")
