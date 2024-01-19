import time

from typing import List

Character = str


def longest_common_subsequence(
    sequence_1: List[Character],
    sequence_2: List[Character]
) -> List[Character]:
    longest_common_subsequence: List[Character] = []

    i = 0
    j = 0
    last_match_j = 0

    max_sequence_1 = len(sequence_1) - 1
    max_sequence_2 = len(sequence_2) - 1

    while i <= max_sequence_1:
        if j > max_sequence_2:
            i += 1
            j = last_match_j
            continue

        # print(i, j)
        if sequence_1[i] == sequence_2[j]:
            longest_common_subsequence.append(sequence_1[i])
            i += 1
            j += 1
            last_match_j = j
        else:
            j += 1

    return longest_common_subsequence


def main() -> None:
    tests = [
        # ("ABCD", "XABD",),
        # ("XABD", "ABCD",),

        # A D E F I K
        #       ▲
        # Notice the positions of the F's
        # ▼
        # F D E I K
        #
        # Depending with which sequence you start
        # the greedy algorithm will spit either
        # - DEIK    :   correct
        # - FIK     :   wrong
        ("ADEFIJK", "FDEIK",),
        ("FDEIK", "ADEFIJK",),
        # ("ABCDEFGHHHHH", "XABDEKKKPPPP",),
        # ("XABDEKKKPPPP", "ABCDEFGHHHHH",),
        # ("ABCDEFGHHHHHZ", "XABDEKKKPPPPZ",),
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
