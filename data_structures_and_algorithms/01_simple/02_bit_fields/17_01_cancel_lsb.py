"""
Cancel least significant bit
"""

if __name__ == '__main__':
    a = 0b00000000
    b = 0b00000001

    CANCEL_MASK = 0xff ^ 0b1

    x = a & CANCEL_MASK
    y = b & CANCEL_MASK

    print(f"a               {a:#0{10}b}")
    print(f"b               {b:#0{10}b}")
    print(f"CANCEL_MASK     {CANCEL_MASK:#0{10}b}")
    print(f"a & CANCEL_MASK {x:#0{10}b}")
    print(f"b & CANCEL_MASK {y:#0{10}b}")
