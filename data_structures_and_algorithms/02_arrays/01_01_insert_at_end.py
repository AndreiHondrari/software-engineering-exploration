from typing import List


if __name__ == '__main__':
    l1: List[int] = [11, 22, 33]
    NEW_ITEM = 777

    l2: List[int] = l1 + [NEW_ITEM]

    print(f"{l1} with {NEW_ITEM} -> {l2}")
