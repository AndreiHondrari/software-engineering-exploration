"""
Fill bits from left
"""


def fill_bits_from_msb(amount: int) -> int:
    result: int = 0xff & (0x00 - 2**(8 - amount))
    return result


if __name__ == '__main__':
    for i in range(8 + 1):
        result = fill_bits_from_msb(i)
        print(f"{i} {result:#0{10}b}")
