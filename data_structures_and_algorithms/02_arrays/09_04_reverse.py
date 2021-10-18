from typing import List


if __name__ == '__main__':
    l1: List[int] = [11,  22,  33,  44,  55,  66,  77,  88,  99]

    print(f"L1 BEFORE: {l1}")

    SIZE: int = len(l1)
    HALF_SIZE: int = SIZE // 2

    for i in range(HALF_SIZE):
        j = SIZE - i - 1

        # xor swap because we're cool
        l1[i] = l1[i] ^ l1[j]
        l1[j] = l1[i] ^ l1[j]
        l1[i] = l1[i] ^ l1[j]

    print(f"L1 AFTER:  {l1}")
