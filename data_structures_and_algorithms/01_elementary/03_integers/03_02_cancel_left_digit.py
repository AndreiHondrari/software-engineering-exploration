"""
We cancel the left digit by obtaining the remainder of the integer division
between our number and 10 to the power of the count of digits of our number
minus 1.

Let's assume 56789 is our number with 5 digits.
10 ** (5 - 1) = 10000

56789 % 10000 = 6789
"""

if __name__ == '__main__':

    a: int = 12345
    DIGITS_COUNT: int = 5

    power_of_ten: int = (DIGITS_COUNT - 1)
    divider: int = 10**power_of_ten
    x = a % divider

    print(f"{a} % {divider} [10**{power_of_ten}] -> {x}")
