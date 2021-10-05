from time import time


def sum_until_limit(limit: int) -> int:
    return int((limit * (limit + 1)) / 2)


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
