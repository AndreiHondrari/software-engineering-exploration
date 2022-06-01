from typing import List


def add_one(digits: List[int]) -> List[int]:
    # handle empty digits array
    if len(digits) == 0:
        return [1]

    least_digit_position = len(digits) - 1
    least_significant_digit = digits[least_digit_position]
    rest_of_digits = digits[0:least_digit_position]

    if least_significant_digit == 9:
        rest_of_digits = add_one(rest_of_digits)
        least_significant_digit = 0
    else:
        least_significant_digit += 1

    return rest_of_digits + [least_significant_digit]


def main() -> None:
    tests = [
        [],
        [2],
        [9],
        [2, 9],
        [9, 9],
        [3, 9, 9],
        [5, 9, 9, 9],
    ]

    for n in tests:
        print(n, add_one(n))


if __name__ == "__main__":
    main()
