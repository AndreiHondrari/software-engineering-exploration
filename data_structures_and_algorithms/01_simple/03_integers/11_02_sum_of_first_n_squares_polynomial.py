from time import time


def sum_of_squares_until_limit(limit: int) -> int:
    return int(
        (1/3) * limit ** 3 +
        (1/2) * limit ** 2 +
        (1/6) * limit
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
