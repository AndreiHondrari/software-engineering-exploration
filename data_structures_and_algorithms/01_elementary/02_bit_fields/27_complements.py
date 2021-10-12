"""
Complements in Python

Sign bits in Python are not part of the bitfield itself but as some
special flag attached to the value, so some operations that you would
do on this number will not affect the bit. You can apply complement on it
and it will flip it. Masking and shifting of
a negative number has some interesting and unexpected behaviour.

~x will result in all the bits flipped, including the sign bit.
This number will be printed out by python with a minus sign and
the positive representation of the rest of the flipped number
(which is not what you would expect -> it is a one's complement, so it's off
by one from the negative of x).

Masking the complement ((~x) & 0xff) will convert the value to unsigned
and allows Python to print the real bit representation of x. It's kind of
inconvenient that one has to do this to see the real bit field representation.
"""

if __name__ == '__main__':
    x = 0b00110101
    print(f"INITIAL           {x:0{8}b} {x: >3}")

    # ±x same as -x-1
    x_complement = ~x
    print(f"One's complement: {x_complement:0{8}b} {x_complement}")

    xcm = x_complement_masked = x_complement & 0xff
    print(f"masked            {xcm:0{8}b} {xcm}")

    xtc = x_twos_complement = (~x) + 1
    print(f"Two's complement: {xtc:0{8}b} {xtc}")

    xtcm = x_twos_complement_masked = x_twos_complement & 0xff
    print(f"masked            {xtcm:0{8}b} {xtcm}")
