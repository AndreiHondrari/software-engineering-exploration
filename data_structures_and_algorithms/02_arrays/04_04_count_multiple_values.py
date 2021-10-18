from typing import List
from random import random as rd
from time import time


if __name__ == '__main__':
    SIZE: int = 10_000_000
    l1: List[int] = [
        int(rd() * 10) % 10
        for _ in range(SIZE)
    ]
    print(f"ORIGINAL: {l1[:20]}... ({SIZE})")

    reference_list: List[int] = [3, 5, 7]
    print(f"REFERENCES: {reference_list}")

    start = time()
    amount: int = 0

    for n in l1:
        for k in reference_list:
            if n == k:
                amount += 1
                break
    stop = time()

    print(f"AMOUNT: {amount}")
    print(f"Count time: {stop-start:.2f}s")
