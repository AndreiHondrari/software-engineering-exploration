"""
LSB - Least Significant Bit
"""

if __name__ == '__main__':

    # define an input
    a = 0b01010010
    b = 0b01010011

    # extract the LSB in a new bit field
    a_lsb_field = a % 2
    b_lsb_field = b % 2

    # detect the truth value of the LSB
    a_lsb: bool = a_lsb_field != 0b0
    b_lsb: bool = b_lsb_field != 0b0

    print(f"a     {a:#0{10}b}")
    print(f"a_lsb {a_lsb}\n")

    print(f"b     {b:#0{10}b}")
    print(f"b_lsb {b_lsb}")
