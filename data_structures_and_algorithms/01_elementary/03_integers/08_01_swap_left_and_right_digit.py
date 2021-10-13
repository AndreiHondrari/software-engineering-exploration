"""

"""


def count_digits(n: int) -> int:
    total_digits_count: int = 0 if n > 0 else 1
    n_copy: int = n
    while n_copy > 0:
        total_digits_count += 1
        n_copy //= 10

    return total_digits_count


if __name__ == '__main__':
    a: int = 52332337
    no_of_digits: int = count_digits(a)

    left_magnitude: int = 10**(no_of_digits - 1)

    left_digit: int = a // left_magnitude
    right_digit: int = a % 10

    x: int = (
        a - left_digit * left_magnitude - right_digit +
        right_digit * left_magnitude + left_digit
    )

    y: int = (
        a +
        left_digit * (1 - left_magnitude) +
        right_digit * (left_magnitude - 1)
    )

    z: int = (
        a % left_magnitude + right_digit * (left_magnitude - 1) + left_digit
    )

    print(f"v1 {a} -> {x}")
    print(f"v2 {a} -> {y}")
    print(f"v3 {a} -> {z}")
