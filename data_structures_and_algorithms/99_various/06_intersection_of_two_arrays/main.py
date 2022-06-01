from typing import List, Dict
from collections import defaultdict


def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    nums1_appearances: Dict[int, int] = defaultdict(int)
    nums2_appearances: Dict[int, int] = defaultdict(int)

    all_values = set()
    for i in range(max(len(nums1), len(nums2))):
        if i < len(nums1):
            n1_value = nums1[i]
            all_values.add(n1_value)
            nums1_appearances[n1_value] += 1

        if i < len(nums2):
            n2_value = nums2[i]
            all_values.add(n2_value)
            nums2_appearances[n2_value] += 1

    print(nums1_appearances)
    print(nums2_appearances)
    print(all_values)
    result = []
    for value in all_values:
        if value in nums1_appearances and value in nums2_appearances:
            cross_count = min(
                nums1_appearances[value],
                nums2_appearances[value]
            )
            values_to_add = [value] * cross_count
            result += values_to_add

    return result


def main() -> None:
    l1 = [1, 2, 2, 1]
    l2 = [2, 2]
    kek = intersect(l1, l2)

    print(kek)


if __name__ == "__main__":
    main()
