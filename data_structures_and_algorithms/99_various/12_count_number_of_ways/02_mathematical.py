"""
Given a number n, determine the number of combinations you can
make by adding up multiples of 1 and 2 that summed up
equal n
"""

"""
It looks like the growth resembles the fibonacci sequence.
To do it mathematically we need to implement a formula that will give us
the n-th fibonacci number of the sequence.

For this we could use Binnet's (1843) formula using the golden ratio.
"""

GOLDEN_RATIO = (1 + 5 ** 0.5) / 2


def binnet_nth(n: int) -> int:
    return int(
        (GOLDEN_RATIO ** n - (-GOLDEN_RATIO) ** (-n)) /
        (5 ** 0.5)
    )


def count_ways(n: int) -> int:
    # we can ignore 0 .. 3
    if n < 4:
        return n

    # must offset by 1 because
    # Jacques P. M. Binnet counted from 1 not 0
    return binnet_nth(n + 1)


def main() -> None:
    for k in range(45 + 1):
        res = count_ways(k)
        print(k, res)


if __name__ == "__main__":
    main()
