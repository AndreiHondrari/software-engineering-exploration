"""
Reverse bits with masks
"""


if __name__ == '__main__':
    a = 0x15
    x = 0x00 | a
    x = (x & 0x55) << 1 | (x & 0xaa) >> 1
    x = (x & 0x33) << 2 | (x & 0xcc) >> 2
    x = (x & 0x0f) << 4 | (x & 0xf0) >> 4

    print(f"INITIAL {a:#0{10}b}")
    print(f"FINAL   {x:#0{10}b}")
