"""
Exchange two bit field parts
"""

if __name__ == '__main__':
    # initially 0110 1001
    INITIAL = 0b01101001
    a = INITIAL

    # extract halves
    first_nibble = a & 0b11110000
    second_nibble = a & 0b00001111

    # shift positions
    first_nibble = first_nibble >> 4
    second_nibble = second_nibble << 4

    # recombine -> to 1001 0110
    a = first_nibble | second_nibble

    print(f"INITIAL {INITIAL:#0{10}b}")
    print(f"FINAL   {a:#0{10}b}")
