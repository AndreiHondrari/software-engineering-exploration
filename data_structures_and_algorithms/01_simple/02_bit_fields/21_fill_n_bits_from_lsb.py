"""
Fill bits from right
"""


def fill_bits_from_lsb(amount: int) -> int:
    result: int = 2**amount - 1
    return result


if __name__ == '__main__':
    for i in range(8 + 1):
        result = fill_bits_from_lsb(i)
        print(f"{i} {result:#0{10}b}")
