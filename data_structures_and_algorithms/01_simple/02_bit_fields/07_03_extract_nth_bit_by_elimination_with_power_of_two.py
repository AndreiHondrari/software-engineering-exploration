"""
Extract nth bit by elimination (through mask)
"""

if __name__ == '__main__':
    # define our bit field
    a = 0b00010000

    # extract the nth bit field (the only 1 bit)
    N = 4  # counting from 0 to 7
    nth_bit = (
        (
            a & (2**N)  # mask the Nth bit
        ) != 0b0  # detect non-nullability
    )

    print(f"nth ({N}) bit: {nth_bit}")
