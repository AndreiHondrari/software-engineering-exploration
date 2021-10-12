
from typing import Tuple


def add_bit(a: bool, b: bool) -> Tuple[bool, bool]:
    result = a ^ b
    carry = a & b
    return (result, carry)


if __name__ == '__main__':

    print("F F: ", add_bit(False, False))
    print("F T: ", add_bit(False, True))
    print("T F: ", add_bit(True, False))
    print("T T: ", add_bit(True, True))
