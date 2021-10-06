"""
Error accumulation
------------------

0.0001 is stored as 0.0001000000000000000047921736

if you sum it for 100_000 times then the result is not 10 as expected but:
9.999999999990033

which used in an operation as exponent, it creates a huge error.
"""

if __name__ == '__main__':
    x = 0.0001
    res = 0
    for i in range(100_000):
        res += x

    print(res)

    N = 567
    expected = N**10
    offval = N**res
    print(f"EXPECTED: {expected:f}")
    print(f"OFF  VAL: {offval:f}")
    print(f"ERROR: {expected-offval:f}")
