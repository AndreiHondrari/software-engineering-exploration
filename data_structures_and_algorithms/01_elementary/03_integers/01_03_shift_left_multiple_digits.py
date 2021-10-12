"""
Shifting to the left multiple digits is done by multiplying with
10 to the power of the amount of digits.

Let's assume our offset is 4.

10 to the power of 4 = 10000

123 * 10000 = 1230000
"""

if __name__ == '__main__':
    a = 12345
    amount = 3
    x = a * 10**amount
    print(f"{a} [{amount}] -> {x}")
