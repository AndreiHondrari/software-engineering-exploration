"""
We can force the rightmost digit to 0 by subtracting from it its last digit.

5678 - 8 = 5670
"""

if __name__ == '__main__':

    a: int = 12345
    x = a - a % 10
    print(f"{a} -> {x}")
