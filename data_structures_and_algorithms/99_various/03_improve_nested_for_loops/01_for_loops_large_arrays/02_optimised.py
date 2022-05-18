import time
import random as rd
from typing import List


def process_lists(
    v1: List[int],
    v2: List[int]
) -> List[int]:
    """
    Time complexity
    2 * O(n * log(n)) + O(1) + O(k) = O(n * log(n))
    """

    out: List[int] = []

    # sorted : O(n * log(n))
    sorted_v1 = list(sorted(v1))
    sorted_v2 = list(sorted(v2))

    # O(1)
    min_length = min(len(sorted_v1), len(sorted_v2))

    # O(k) where k <= n
    for i in range(min_length):
        if sorted_v1[i] == sorted_v2[i]:
            # append: O(1)
            out.append(sorted_v1[i])

    return out


def main() -> None:
    print("Generate v1 ...")
    v1 = [rd.randint(0, 100) for x in range(1_000_000)]

    print("Generate v2 ...")
    v2 = [rd.randint(0, 100) for x in range(1_000_000)]

    print("Process v1, v2 ...")
    start = time.time()
    v3 = process_lists(v1, v2)
    stop = time.time()

    print(len(v3))

    print(f"Elapsed {stop-start:.2f} seconds")


if __name__ == "__main__":
    main()
