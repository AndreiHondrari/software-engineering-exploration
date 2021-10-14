from typing import List


def count_digits(n: int) -> int:
    total_digits_count: int = 0 if n > 0 else 1
    n_copy: int = n
    while n_copy > 0:
        total_digits_count += 1
        n_copy //= 10

    return total_digits_count


if __name__ == '__main__':
    a: int = 1234
    no_of_digits: int = count_digits(a)
    new_digits: List[int] = [
        9, 4, 8, 5, 7,
    ]

    x: int = a
    for d in new_digits:
        x = x + d * 10**no_of_digits
        no_of_digits += 1

    print(f"{a} with {new_digits} -> {x}")
