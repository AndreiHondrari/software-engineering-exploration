"""
n = 123456

x = 123456
x = 623451
x = 653421
x = 654321
"""


def count_digits(n: int) -> int:
    total_digits_count: int = 0 if n > 0 else 1
    n_copy: int = n
    while n_copy > 0:
        total_digits_count += 1
        n_copy //= 10

    return total_digits_count


def swap_digits(n: int, offset_1: int, offset_2: int) -> int:
    first_magnitude: int = 10**offset_1
    second_magnitude: int = 10**offset_2

    first_digit: int = n // first_magnitude % 10
    second_digit: int = n // second_magnitude % 10

    old_first = first_digit * first_magnitude
    old_second = second_digit * second_magnitude

    new_first = second_digit * first_magnitude
    new_second = first_digit * second_magnitude

    return n - old_first - old_second + new_first + new_second


if __name__ == '__main__':
    a: int = 123456789
    no_of_digits: int = count_digits(a)

    x: int = a
    for i in range(no_of_digits // 2):
        x = swap_digits(x, no_of_digits - i - 1, i)

    print(f"{a} -> {x}")
