from typing import List
from random import random as rd
from time import time


if __name__ == '__main__':
    SIZE: int = 10_000_000
    l1: List[int] = [
        int(rd() * 10) % 10
        for _ in range(SIZE)
    ]
    l1 = list(sorted(l1))
    print(f"ORIGINAL: {l1[:20]}... ({SIZE})")

    reference_list: List[int] = [3, 5, 7]
    print(f"REFERENCES: {reference_list}")

    start = time()

    amount: int = 0
    ref_index: int = 0
    l1_index: int = 0

    rlist_size: int = len(reference_list)
    l1_size: int = len(l1)

    while ref_index < rlist_size and l1_index < l1_size:
        k = reference_list[ref_index]
        n = l1[l1_index]

        if n > k:
            ref_index += 1
            continue

        if n == k:
            amount += 1

        l1_index += 1

    stop = time()

    print(f"AMOUNT: {amount}")
    print(f"Count time: {stop-start:.2f}s")
