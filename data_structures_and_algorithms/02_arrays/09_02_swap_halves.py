from typing import List


def swap_halves(vals: List[int]):
    SIZE: int = len(vals)
    HALF_SIZE: int = SIZE // 2
    offset_by_1: bool = SIZE % 2 != 0
    offset_term: int = 1 if offset_by_1 else 0
    for i in range(HALF_SIZE):
        j = HALF_SIZE + offset_term + i

        # xor swap because we're cool
        vals[i] = vals[i] ^ vals[j]
        vals[j] = vals[i] ^ vals[j]
        vals[i] = vals[i] ^ vals[j]


if __name__ == '__main__':
    l1: List[int] = [11,  22,  33,  44,  55,  66,  77,  88,  99]

    print(f"L1 BEFORE: {l1}")
    swap_halves(l1)
    print(f"L1 AFTER:  {l1}")

    print()

    l2: List[int] = [111, 222, 333, 444, 555, 666]
    print(f"L2 BEFORE: {l2}")
    swap_halves(l2)
    print(f"L2 AFTER:  {l2}")
