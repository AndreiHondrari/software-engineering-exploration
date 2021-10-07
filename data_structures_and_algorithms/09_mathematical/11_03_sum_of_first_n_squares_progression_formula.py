from time import time
from decimal import Decimal as D


def sum_of_squares_until_limit(limit: int) -> int:
    return int(
        D(limit * (limit + 1) * (2 * limit + 1)) / D(6)
    )


if __name__ == '__main__':
    numbers = [
        5, 10, 1_000_000, 5_000_000,
    ]
    for n in numbers:
        a = time()
        result = sum_of_squares_until_limit(n)
        b = time()
        print(f"{n} => {result} [{b-a:.2f}]s")
