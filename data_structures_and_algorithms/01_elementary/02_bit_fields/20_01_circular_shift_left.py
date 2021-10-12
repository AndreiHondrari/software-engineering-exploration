
def shift_left(
    value: int,
    number_of_bits: int
) -> int:
    # assume the input is 1 byte
    assert value <= 0xff

    number_of_bits = number_of_bits % 8

    # obtain left part by shifting for the necessary amount of bits
    # and mask to be sure it's 1 byte
    left_part = (value << number_of_bits) & 0xff

    # obtain right part by shifting completely to the right by 8 bits
    # and then just offset by the desired shift amount
    right_part = value >> (8 - number_of_bits)

    # recombine left and right into the final result
    final: int = left_part | right_part
    return final


if __name__ == '__main__':
    x = 0xf0
    print(f"INITIAL {x:#0{10}b}")

    for i in range(-8, 8):
        result = shift_left(x, i)
        print(f"{i: >2}      {result:#0{10}b}")
