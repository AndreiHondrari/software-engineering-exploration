"""
n = 1234
no_of_digits = 4

x = 0

x = x + 1234 // 1 % 10 * 1000 = 4000
x = x + 1234 // 10 % 10 * 100 = 4300
x = x + 1234 // 100 % 10 * 10 = 4320
x = x + 1234 // 1000 % 10 * 1 = 4321
"""


def count_digits(n: int) -> int:
    # count digits
    total_digits_count: int = 0 if n > 0 else 1
    n_copy: int = n
    while n_copy > 0:
        total_digits_count += 1
        n_copy //= 10

    return total_digits_count


if __name__ == '__main__':
    a: int = 123456789
    no_of_digits: int = count_digits(a)

    x: int = 0
    for i in range(no_of_digits):
        # determine magnitudes for old position and new position
        current_magnitude: int = 10**i
        next_magnitude: int = 10**(no_of_digits - 1 - i)

        # extract digit
        digit: int = a // current_magnitude % 10

        # reconstruct
        x += digit * next_magnitude

    print(f"{a} -> {x}")
