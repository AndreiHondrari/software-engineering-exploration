"""

n = 111 777
offset1 = 3
offset2 = 1

a = 111777 // 10**3 % 10 = 1
b = 111777 // 10**1 % 10 = 7

c = 7 * 10**3 = 7000
d = 1 * 10**1 = 10

e = 1 * 10**3 = 1000
f = 7 * 10**1 = 70

g = n - a - b = 111777 - 1000 - 70 = 110707

g + c + d = 110707 + 7000 + 10 = 117717
"""


if __name__ == '__main__':
    a: int = 111_777
    offset1: int = 1
    offset2: int = 3

    # magnitudes
    first_magnitude: int = 10**offset1
    second_magnitude: int = 10**offset2

    # extract digits
    first_digit = a // first_magnitude % 10
    second_digit = a // second_magnitude % 10

    # calculate new digits shifted in position
    new_first = second_digit * first_magnitude
    new_second = first_digit * second_magnitude

    # calculate old digits shifted in position
    first = first_digit * first_magnitude
    second = second_digit * second_magnitude

    # combine partial results
    x: int = a - first - second + new_first + new_second

    print(f"{a} -> {x}")
