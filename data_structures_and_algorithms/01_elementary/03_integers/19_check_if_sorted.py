from typing import List


def count_digits(n: int) -> int:
    total_digits_count: int = 0 if n > 0 else 1
    n_copy: int = n
    while n_copy > 0:
        total_digits_count += 1
        n_copy //= 10

    return total_digits_count


def is_sorted(n: int) -> bool:
    no_of_digits: int = count_digits(n)
    for i in range(no_of_digits - 1):
        p = int(n // 10**(no_of_digits - i - 1) % 10)
        q = int(n // 10**(no_of_digits - i - 2) % 10)
        if p > q:
            return False

    return True


if __name__ == '__main__':
    numbers: List[int] = [
        12,
        123,
        1234,
        2134,
        1243,
        57381579275,
        1112223334445556667778889999,
    ]
    for n in numbers:
        x: int = is_sorted(n)
        print(f"{str(x): <6}: {n}")
