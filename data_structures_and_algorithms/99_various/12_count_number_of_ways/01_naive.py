"""
Given a number n, determine the number of combinations you can
make by adding up multiples of 1 and 2 that summed up
equal n
"""

from typing import List, Optional


def count_ways(
    n: int,
    steps_left: Optional[int] = None,
    steps: Optional[List[int]] = None
) -> int:

    if steps_left is None:
        steps_left = n

    if steps is None:
        steps = []

    steps_match = sum(steps) == n
    this_count = 1 if steps_match else 0

    if steps_left == 0:
        return this_count

    count_a = count_ways(n, steps_left - 1, steps + [1])
    count_b = count_ways(n, steps_left - 1, steps + [2])

    return this_count + count_a + count_b


def main() -> None:
    for k in range(10):
        res = count_ways(k)
        print(k, res)

    # N = 35
    # res = count_ways(N)
    # print(N, res)


if __name__ == "__main__":
    main()
