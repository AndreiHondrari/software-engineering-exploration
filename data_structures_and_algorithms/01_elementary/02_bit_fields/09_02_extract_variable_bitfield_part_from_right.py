"""
Extract variable number of bits from a bitfield - from LSB
"""


def extract_bits_from_lsb(
    value: int,
    pivot: int,
    number_of_bits: int
) -> int:
    # make sure that we deal with maximum 8 bits
    assert value <= 0b11111111, "bitfield must have a maximum size of 8 bits"

    # make sure the pivot is not out of bound
    assert pivot <= 7

    # make sure that we are not overflowing with the offset from the pivot
    MAX_BITS_FROM_PIVOT = 8 - pivot
    assert 0 <= number_of_bits <= MAX_BITS_FROM_PIVOT, \
        "number of bits must be in range 0 .. (8 - pivot)"

    # initialize our extracted bitfield
    extracted: int = 0b0

    # sweep over the bits from pivot to the right (as many bits as required)
    for i in range(number_of_bits):
        nth_bitfield = value & (0b1 << (i + pivot))
        extracted = extracted | nth_bitfield

    return extracted


if __name__ == '__main__':
    a = 0b11111111

    res1: int = extract_bits_from_lsb(a, 0, 0)
    res2: int = extract_bits_from_lsb(a, 0, 8)
    res3: int = extract_bits_from_lsb(a, 3, 4)

    print(f"Value   : {a:#0{10}b}")
    print(f"Part 0 0: {res1:#0{10}b}")
    print(f"Part 0 8: {res2:#0{10}b}")
    print(f"Part 3 4: {res3:#0{10}b}")
