"""
Replace bit field part
"""


if __name__ == '__main__':
    # define our input 0101 0110
    INITIAL = 0b01010110
    x = INITIAL

    # define our replacement 0000 0011
    REPLACEMENT = 0b00000011

    # cancel bits in the replaceable part
    CANCEL_MASK = 0b11110000
    x = CANCEL_MASK & x

    # replace
    x = x | REPLACEMENT

    print(f"INITIAL     {INITIAL:#0{10}b}")
    print(f"REPLACEMENT {REPLACEMENT:#0{10}b}")
    print(f"MASK        {CANCEL_MASK:#0{10}b}")
    print(f"FINAL       {x:#0{10}b}")
