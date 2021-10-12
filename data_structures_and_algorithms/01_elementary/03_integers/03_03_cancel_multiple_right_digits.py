"""
We can force multiple rightmost digits by subtracting from the number
a number representing those digits.

123456 - 456 = 123000
"""

if __name__ == '__main__':

    a: int = 123456789
    amount: int = 4
    x = a - a % 10**amount
    print(f"{a} -> {x}")
