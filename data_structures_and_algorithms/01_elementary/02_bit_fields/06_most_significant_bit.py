"""
MSB - Most Significant Bit
"""

if __name__ == '__main__':

    # define an input
    a = 0b00010101
    b = 0b10010101

    # extract the LSB in a new bit field
    MSB_MASK = 0b10000000
    a_msb_field = MSB_MASK & a
    b_msb_field = MSB_MASK & b

    # detect the truth value of the MSB
    a_msb: bool = a_msb_field != 0b0
    b_msb: bool = b_msb_field != 0b0

    print(f"a     {a:#0{10}b}")
    print(f"a_msb {a_msb}\n")

    print(f"b     {b:#0{10}b}")
    print(f"b_msb {b_msb}")
