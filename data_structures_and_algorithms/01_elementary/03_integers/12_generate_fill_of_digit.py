"""

"""


def generate_fill(
    digit: int,
    no_of_digits: int
) -> int:
    assert 1 <= digit <= 9, "digit must be in range 1..9"
    result: int = 0

    for i in range(no_of_digits):
        result += digit * 10**i

    return result


if __name__ == '__main__':
    AMOUNT: int = 29
    for i in range(1, 9+1):
        x: int = generate_fill(i, AMOUNT)
        print(x)
