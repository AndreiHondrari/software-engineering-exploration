"""
Overwrite the n-th digit from the right by

n = 4444
offset = 2

Scenario 1:
(4444 // 1000) * 1000 + 4444 % 100 + 7 * 100
4000 + 44 + 700 = 4744

Scenario 2:
(4444 - (4444 // 100 % 10) * 100) + 7 * 100
(4444 - 400) + 700

"""

if __name__ == '__main__':
    a: int = 555_555_555
    new_digit: int = 7
    offset: int = 6

    # positional magnitude - falls directly on the digit we are interested in
    positional_magnitude: int = 10**offset

    # extra magnitude - positional magnitude + 1
    extra_magnitude: int = 10**(offset + 1)

    x: int = (
        (a // extra_magnitude) * extra_magnitude +
        a % positional_magnitude +
        new_digit * positional_magnitude
    )

    y: int = (
        a - (a // positional_magnitude % 10) * positional_magnitude +
        new_digit * positional_magnitude
    )

    print(f"v1 {a} with {new_digit} -> {x}")
    print(f"v2 {a} with {new_digit} -> {y}")
