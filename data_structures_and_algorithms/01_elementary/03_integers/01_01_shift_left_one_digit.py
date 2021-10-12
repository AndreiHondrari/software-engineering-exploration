"""
Shifting numbers to the left while adding 0s at the right end can be
achieved using multiplication with 10.

123 * 10 = 1230
"""

if __name__ == '__main__':
    a = 12345
    x = a * 10
    print(f"{a} -> {x}")
