"""

"""
from typing import List


def generate_alternating_digits(
    no_of_digits: int,
    digits: List[int]
) -> int:

    result: int = 0

    for i in range(no_of_digits):
        index: int = i % len(digits)
        result += digits[index] * 10**i

    return result


if __name__ == '__main__':
    AMOUNT = 29
    x: int = generate_alternating_digits(29, [3, 5, 7, 9])
    print(x)
