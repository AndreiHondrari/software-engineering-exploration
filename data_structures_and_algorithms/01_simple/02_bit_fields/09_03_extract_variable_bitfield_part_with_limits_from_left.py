"""
Extract variable number of bits from a bitfield (with limits) - from MSB
"""


def extract_bits_from_msb(
    value: int,
    start: int,
    stop: int
) -> int:
    # make sure that we deal with maximum 8 bits
    assert value <= 0b11111111, "bitfield must have a maximum size of 8 bits"

    # make sure the start is not out of bound
    assert start <= 7, "start is out of bound"

    # make sure the stop is not out of bound
    assert stop <= 7, "stop is out of bound"

    # make sure the start is less then or equal to the stop
    assert start <= stop, "start must be less then or equal to stop"

    extracted: int = 0b0

    # sweep over the bits from pivot to the right (as many bits as required)
    for i in range(stop-start+1):
        nth_bitfield = value & (0b10000000 >> (i + start))
        extracted = extracted | nth_bitfield

    return extracted


if __name__ == '__main__':
    a = 0b11111111

    res1: int = extract_bits_from_msb(a, 0, 0)
    res2: int = extract_bits_from_msb(a, 0, 2)
    res3: int = extract_bits_from_msb(a, 0, 7)
    res4: int = extract_bits_from_msb(a, 4, 6)

    print(f"Value   : {a:#0{10}b}")
    print(f"Part 0 0: {res1:#0{10}b}")
    print(f"Part 0 2: {res2:#0{10}b}")
    print(f"Part 0 7: {res3:#0{10}b}")
    print(f"Part 4 6: {res4:#0{10}b}")
