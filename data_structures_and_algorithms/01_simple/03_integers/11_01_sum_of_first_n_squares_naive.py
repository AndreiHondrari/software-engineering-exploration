from time import time


def sum_of_squares_until_limit(limit: int) -> int:
    result = 0
    for x in range(limit + 1):
        result = result + x ** 2
    return result


if __name__ == '__main__':
    numbers = [
        5, 10, 1_000_000, 5_000_000,
    ]
    for n in numbers:
        a = time()
        result = sum_of_squares_until_limit(n)
        b = time()
        print(f"{n} => {result} [{b-a:.2f}]s")
