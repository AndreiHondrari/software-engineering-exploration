"""
Reverse bits
"""


if __name__ == '__main__':
    a = 0x15
    x = 0x00

    NO_OF_BYTES = 1
    NO_OF_BITS = NO_OF_BYTES * 8
    for i in range(NO_OF_BITS):

        # isolate the bit at position i
        isolated_bit_field = a & (0b1 << i)

        # offset the bit from position i to the target position
        # NO_OF_BITS - 1 because range is 0..7
        j = NO_OF_BITS - 1 - i
        offset = j - i
        if offset >= 0:
            isolated_bit_field = (isolated_bit_field << offset)
        else:
            isolated_bit_field = (isolated_bit_field >> -offset)

        # apply resulting bit field to result
        x = x | isolated_bit_field

    print(f"INITIAL {a:#0{2 + NO_OF_BITS}b}")
    print(f"FINAL   {x:#0{2 + NO_OF_BITS}b}")
