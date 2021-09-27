"""
Fill bits from left
"""


def fill_bits_from_msb(
    amount: int,
    number_of_bytes: int
) -> int:
    number_of_bits = 8 * number_of_bytes
    top_value = 2**(8 * number_of_bytes) - 1
    cancel_mask = (2**(number_of_bits - amount) - 1)
    result: int = top_value - cancel_mask
    return result


if __name__ == '__main__':
    NUMBER_OF_BYTES = 2
    for i in range(8 * NUMBER_OF_BYTES + 1):
        result = fill_bits_from_msb(i, NUMBER_OF_BYTES)
        print(f"{i: >2} {result:#0{2+8*NUMBER_OF_BYTES}b}")
