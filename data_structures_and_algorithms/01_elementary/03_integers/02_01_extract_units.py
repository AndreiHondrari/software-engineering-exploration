"""
The remainder of the division of a number and 10 is the rightmost digit of
our number.

159 % 10 = 9
"""

if __name__ == '__main__':
    numbers = [
        5, 10, 17, 289
    ]

    for n in numbers:
        result = n % 10
        print(f"{n} -> {result}")
