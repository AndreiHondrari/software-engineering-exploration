"""
Exchange two bit field parts
"""

if __name__ == '__main__':
    # initially 0110 1001
    INITIAL = 0b01101001
    a = INITIAL

    # extract halves
    first_half = a & 0b11110000
    second_half = a & 0b00001111

    # shift positions
    first_half = first_half >> 4
    second_half = second_half << 4

    # recombine -> to 1001 0110
    a = first_half | second_half

    print(f"INITIAL {INITIAL:#0{10}b}")
    print(f"FINAL   {a:#0{10}b}")
