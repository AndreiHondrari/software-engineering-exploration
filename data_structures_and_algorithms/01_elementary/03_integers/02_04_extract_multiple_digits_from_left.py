"""
To extract an amount of digits starting from the most significant digit
of a number, we must know beforehand the number of digits of the number.

We extract the digits by performing integer division of the number with
10 to the power of the total count of digits
minus the desired amount of digits.


Let's assume a number 56789 which has 5 digits.
We want to get 3 digits.
10 ** (5 - 3) = 100
56789 // 100 = 567
"""

if __name__ == '__main__':

    a = 123456789
    DIGIT_COUNT = 9
    amount = 3
    x = a // 10**(DIGIT_COUNT - amount)
    print(f"{a} [{amount}] -> {x}")
