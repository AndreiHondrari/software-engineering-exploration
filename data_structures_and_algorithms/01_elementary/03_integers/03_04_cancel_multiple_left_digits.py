"""
We cancel multiple left digits by obtaining the remainder of the
integer division between our number and
10 to the power of the count of digits of our number
minus the amount of digits that we want eliminated.

Let's assume 56789 is our number with 5 digits.
We want to eliminate 3 digits from the left.
10 ** (5 - 3) = 10**2 = 100

56789 % 100 = 89
"""

if __name__ == '__main__':

    a: int = 123456789
    DIGITS_COUNT: int = 9
    amount: int = 4

    x = a % 10**(DIGITS_COUNT - amount)
    print(f"{a} [{amount}] -> {x}")
