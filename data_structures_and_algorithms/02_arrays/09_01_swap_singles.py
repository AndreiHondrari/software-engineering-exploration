from typing import List


if __name__ == '__main__':
    l1: List[int] = [11,  22,  33,  44,  55,  66,  77,  88,  99]

    first_index: int = 2
    second_index: int = 8

    print(f"L1 BEFORE: {l1}")

    # xor swap because we're cool
    l1[first_index] = l1[first_index] ^ l1[second_index]
    l1[second_index] = l1[first_index] ^ l1[second_index]
    l1[first_index] = l1[first_index] ^ l1[second_index]

    print(f"L1 AFTER:  {l1}")
