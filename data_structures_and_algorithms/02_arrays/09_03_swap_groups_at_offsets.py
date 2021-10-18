from typing import List


if __name__ == '__main__':
    l1: List[int] = [
        11,  22,  33,  44,  55,  66,  77,  88,  99,
        111, 222, 333, 444, 555, 666, 777, 888, 999,
    ]
    GROUP_OFFSET_1: int = 2
    GROUP_OFFSET_2: int = 14
    AMOUNT: int = 3

    print(f"L1 BEFORE {l1}")

    for i in range(AMOUNT):
        p = GROUP_OFFSET_1 + i
        q = GROUP_OFFSET_2 + i

        # xor swap because we're cool
        l1[p] = l1[p] ^ l1[q]
        l1[q] = l1[p] ^ l1[q]
        l1[p] = l1[p] ^ l1[q]

    print(f"L1 AFTER  {l1}")
