from time import time


def sum_until_limit(limit: int) -> int:
    return int(
        0.5 * limit ** 2 + 0.5 * limit
    )


if __name__ == '__main__':
    numbers = [
        5, 10, 10_000_000, 50_000_000,
        100_000_000, 1_000_000_000,
    ]

    for n in numbers:
        a = time()
        result = sum_until_limit(n)
        b = time()
        print(f"{n} => {result} [{b-a:.2f}]s")
