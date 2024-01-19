import time

from typing import List

Character = str


def display_lcs_table(
    lcs_table: List[List[int]],
    x_dim: int,
    y_dim: int
):
    for j in range(y_dim):
        for i in range(x_dim):
            print(lcs_table[i][j], end="")
            print(" ", end="")

        print()

    print()


def longest_common_subsequence(
    sequence_1: List[Character],
    sequence_2: List[Character]
) -> List[Character]:
    longest_common_subsequence: List[Character] = []

    s1_len = len(sequence_1)
    s2_len = len(sequence_2)

    lcs_table: List[List[int]] = [
        [0 for j in range(s2_len)]
        for i in range(s1_len)
    ]

    # preprocess sequences

    for i in range(s1_len):
        for j in range(s2_len):
            left = i - 1
            up = j - 1

            if sequence_1[i] == sequence_2[j]:
                diagonal_value = 0
                if left >= 0 and up >= 0:
                    diagonal_value = lcs_table[left][up]
                lcs_table[i][j] = diagonal_value + 1

            else:
                left_val = 0
                up_val = 0

                if left >= 0:
                    left_val = lcs_table[left][j]

                if up >= 0:
                    up_val = lcs_table[i][up]

                lcs_table[i][j] = max(left_val, up_val)

    # display_lcs_table(lcs_table, s1_len, s2_len)

    # follow the path of least resistance
    i = s1_len - 1
    j = s2_len - 1

    while i >= 0 and j >= 0:
        left = i - 1
        up = j - 1

        left_val = 0 if left < 0 else lcs_table[left][j]
        up_val = 0 if up < 0 else lcs_table[i][up]
        diagonal_value = 0 if left < 0 or up < 0 else lcs_table[left][up]

        if left_val == up_val:
            if sequence_1[i] == sequence_2[j]:
                longest_common_subsequence.append(sequence_1[i])
            i = left
            j = up
        elif left_val > up_val:
            i = left
        else:
            j = up

        if left_val == 0 and up_val == 0:
            break

    longest_common_subsequence = list(reversed(longest_common_subsequence))

    return longest_common_subsequence


def main() -> None:
    tests = [
        ("XA", "AA",),
        ("AA", "XA",),
        ("ABCD", "XABD",),
        ("XABD", "ABCD",),
        ("ABHHZ", "ABKKZ",),
        ("ADEFIJK", "FDEIKZ",),
        ("FDEIK", "ADEFIJK",),
        ("ABCDEFGHHHHH", "XABDEKKKPPPP",),
        ("XABDEKKKPPPP", "ABCDEFGHHHHH",),
        ("ABCDEFGHHHHHZ", "XABDEKKKPPPPZ",),
    ]

    for t in tests:
        sequence_1: List[Character] = [character for character in t[0]]
        sequence_2: List[Character] = [character for character in t[1]]
        start = time.time()
        lcs: List[Character] = longest_common_subsequence(
            sequence_1,
            sequence_2
        )
        stop = time.time()

        lcs: str = "".join(lcs)
        print(f"[{stop - start:.2f} s] LCS for {t[0]} and {t[1]}: {lcs}")


if __name__ == "__main__":
    main()
