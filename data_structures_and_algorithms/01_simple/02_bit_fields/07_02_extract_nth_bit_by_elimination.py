"""
Extract nth bit by elimination (through mask)
"""

if __name__ == '__main__':
    # define our bit field
    a = 0b00010000

    # extract the nth bit field (the only 1 bit)
    N = 5
    nth_bit = (
        (
            a & (0b1 << (N-1))  # mask the Nth bit
        ) != 0b0  # detect non-nullability
    )

    print(f"nth ({N}) bit: {nth_bit}")
