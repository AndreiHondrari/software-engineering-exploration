from typing import List


def single_number(nums: List[int]) -> int:

    if len(nums) == 1:
        return nums[0]

    nums = sorted(nums)
    print(nums)

    i = 1
    target = nums[0]
    genuine_target = True
    current = target

    while i < len(nums):
        other = nums[i]
        if current != other:
            if genuine_target:
                return target  # we found it
            else:
                target = other
                current = other
                genuine_target = True
        else:
            genuine_target = False

        print(i, target, current, other, genuine_target)
        i += 1

    return target


def main() -> None:
    nums = [2, 2, 1]
    val = single_number(nums)
    print(val)


if __name__ == "__main__":
    main()
