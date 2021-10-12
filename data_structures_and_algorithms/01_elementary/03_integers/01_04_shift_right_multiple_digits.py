"""
Shifting to the right multiple digits can be performed by integer division with
10 to the power of the number of digits to be shifted.

Let's assume our offset is 2

10 to the power of 2 is 100

123456789 // 100 = 1234567
"""

if __name__ == '__main__':
    a = 12345
    amount = 3
    x = a // 10**amount
    print(f"{a} -> {x}")
