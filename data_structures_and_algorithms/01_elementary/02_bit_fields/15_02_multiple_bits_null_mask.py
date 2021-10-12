"""
Obtain a "negative" mask where multiple bits are 0
"""

if __name__ == '__main__':
    OFFSET = 3
    NO_OF_BITS = 4

    # create a mask pattern that can be shiften for canceling bits
    mask = 0x00
    for i in range(NO_OF_BITS):
        mask = mask | (0b1 << i)

    # 0xff is equivalent with 0b11111111
    # finally cancel out the desired bits
    x = 0xff ^ (mask << OFFSET)

    print(f"{x:#0{10}b}")
