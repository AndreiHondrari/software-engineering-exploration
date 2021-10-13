"""

Scenario 1 (even amount of digits):

n = 1122
no_of_digits = 4

a = 10 ** (4 // 2) = 100
b = 10 ** (4 // 2) = 100

c = 1122 // 100 = 11
d = 1122 % 100 * 100 = 2200

c + d = 11 + 2200 = 2211


Scenario 2 (odd amount of digits):

n = 11322
no_of_digits = 5

a = 10 ** (4 // 2 + 1) = 1000
b = 10 ** (4 // 2) = 100

c = 11322 // 1000 = 11
d = 11322 % 100 * 1000= 22000

e = 11322 // 100 % 10 * 10 = 300

c + d + e = 22000 + 11 + 300 = 22311

"""


def count_digits(n: int) -> int:
    total_digits_count: int = 0 if n > 0 else 1
    n_copy: int = n
    while n_copy > 0:
        total_digits_count += 1
        n_copy //= 10

    return total_digits_count


def swap_halves(n: int) -> int:
    no_of_digits: int = count_digits(n)

    # for cases where there is digit in the middle
    is_even: bool = no_of_digits % 2 == 0

    left_magnitude = 10**(no_of_digits // 2 + (0 if is_even else 1))
    right_magnitude = 10**(no_of_digits // 2)

    # extract existing left and shift it to the right
    new_right_half: int = n // left_magnitude

    # extract existing right and shift it to the left
    new_left_half: int = n % right_magnitude * left_magnitude

    # extract existing middle and cancel all other digits
    middle: int = 0 if is_even else (
        n // right_magnitude % 10 * right_magnitude
    )

    # combine partial results
    return new_left_half + middle + new_right_half


if __name__ == '__main__':
    numbers = [
        1,
        5,
        15,
        1_2_3,
        11_22,
        11_3_22,
        55_7_88,
    ]

    for n in numbers:
        result: int = swap_halves(n)
        print(f"{n} -> {result}")
