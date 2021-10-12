"""
Due to the nature of how floating point numbers are represented in
binary (standard IEEE 754), some numbers are represented to a very long
precision (28 digits after the floating-point), which makes
the CPU approximate that representation.

To deal with this problem, it is important to know what degree of precision
we need for our software, and round the number to that precision.
"""

if __name__ == '__main__':
    a: float = 0.1
    b: float = 0.2
    res: float = a + b
    res_corrected: float = round(res, 8)

    print(f"a {a}")
    print(f"b {b}")
    print(f"a + b = {res}")
    print(f"a + b (round-off correction) = {res_corrected}")
