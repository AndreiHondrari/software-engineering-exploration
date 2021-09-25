"""
Extract nth bit by extracting from LSB
"""

if __name__ == '__main__':
    # define our bit field
    a = 0b00010000

    # extract the nth bit field (the only 1 bit)
    N = 5
    nth_bit = (
        (
            (
                a >> (N - 1)  # shift to LSB position the Nth bit
            ) & 0b1  # mask it out
        ) != 0b0  # detect non-nullability
    )

    print(f"nth ({N}) bit: {nth_bit}")
