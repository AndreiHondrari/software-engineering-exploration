from typing import List


def reverse(nums: List[int], a: int, b: int):
    """
    Fast reverse by reversing from the edges
    towards the middle
    """
    if a >= b:
        return

    i = a
    j = b
    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1


def rotate(nums: List[int], k: int) -> None:
    """
    The idea is to do section reversals:
    - reverse whole array
    - reverse first k elements
    - reverse the rest of the elements from k+1 onwards

    The result is a right shifted array.
    """
    if k == 0:
        return

    new_k = k
    if k >= len(nums):
        new_k = k % len(nums)

    reverse(nums, 0, len(nums) - 1)
    reverse(nums, 0, new_k - 1)
    reverse(nums, new_k, len(nums) - 1)


def main() -> None:
    nums = [1, 2, 3, 4, 5, 6, 7]
    rotate(nums, 3)

    print(nums)


if __name__ == "__main__":
    main()
