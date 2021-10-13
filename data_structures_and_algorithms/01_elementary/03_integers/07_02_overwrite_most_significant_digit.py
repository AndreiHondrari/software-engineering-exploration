"""
Overwrite the most significant digit by removing it first and then
adding the new digit multiplied with 10 to the power of the number of
digits in our number, minus one

n = 444 with 3 digits

Scenario 1:
444 % (10 ** (3 - 1)) + 7 * (10 ** (3 - 1))
444 % 100 + 7 * 100 = 744

Scenario 2:
444 - (444 // 10 ** (3 - 1)) * 10 ** (3 - 1) + 7 * (10 ** (3 - 1))
444 - 400 + 700 = 744
"""

if __name__ == '__main__':
    a: int = 2
    new_digit: int = 7

    # count digits
    total_digits_count: int = 0 if a > 0 else 1
    n_copy: int = a
    while n_copy > 0:
        total_digits_count += 1
        n_copy //= 10

    magnitude: int = 10 ** (total_digits_count - 1)

    x: int = (
        (a % magnitude) +
        (new_digit * magnitude)
    )

    y: int = (
        (a - (a // magnitude) * (magnitude)) +
        (new_digit * magnitude)
    )

    print(f"v1 {a} with {new_digit} -> {x}")
    print(f"v2 {a} with {new_digit} -> {y}")
