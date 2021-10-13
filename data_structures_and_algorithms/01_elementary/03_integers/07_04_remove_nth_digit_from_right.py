"""

n = 111222
offset = 3

111222 - (111222 - 111222 % 10**3) + (111222 // 10**4) * 10**3
111222 - 111000 + 11000 = 11222

which simplified is
111222 % 10**3 + (111222 // 10**4) * 10**3
222 + 11000 = 11222
"""

if __name__ == '__main__':
    a: int = 123_456_789
    offset: int = 5

    positional_magnitude: int = 10 ** offset
    extra_magnitude: int = 10 ** (offset + 1)

    x: int = (
        a % positional_magnitude +
        (a // extra_magnitude) * positional_magnitude
    )

    print(f"{a} at index {offset} -> {x}")
