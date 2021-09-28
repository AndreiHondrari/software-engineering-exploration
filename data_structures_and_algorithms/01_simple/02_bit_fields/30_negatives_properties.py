"""
Negations lead to interesting properties
-0 is 0b 0000 0000 in binary because there is no complement on the
negative side for zeroes, BUT
-1 is 0b 1111 1111 in binary, because two's complement of 1 is
1 bit for the negative sign and 0xEF for the rest of the byte
to represent the negative one.

0111 1111 +127
...       +...
0000 0001 +1
0000 0000 0
1111 1111 -1
1111 1110 -2
1111 1101 -3
1111 1100 -4
...
1000 0000 -128
"""

if __name__ == '__main__':
    # masking examples with 0xFF to extract the bits and
    # discard the Python sign flag

    a = 0
    b = 1

    neg_a = -a
    neg_b = -b

    print(f"Negative of 0: {neg_a & 0xff:#0{10}b}")
    print(f"Negative of 1: {neg_b & 0xff:#0{10}b}\n")

    n = 127
    print(f"{n: >4}: {n & 0xFF:#0{10}b}")

    n = 2
    print(f"{n: >4}: {n & 0xFF:#0{10}b}")

    n = 1
    print(f"{n: >4}: {n & 0xFF:#0{10}b}")

    n = 0
    print(f"{n: >4}: {n & 0xFF:#0{10}b}")

    n = -1
    print(f"{n: >4}: {n & 0xFF:#0{10}b}")

    n = -2
    print(f"{n: >4}: {n & 0xFF:#0{10}b}")

    n = -3
    print(f"{n: >4}: {n & 0xFF:#0{10}b}")

    n = -4
    print(f"{n: >4}: {n & 0xFF:#0{10}b}")

    n = -128
    print(f"{n: >4}: {n & 0xFF:#0{10}b}")

    # This is because in Python the sign is kept somewhere else.
    # In C, you would not be able to assign 128, because it would flip to
    # -128 naturally
    print(f"128 (0b1000 0000) == -128 (0b1000 0000): {128 == -128}")
