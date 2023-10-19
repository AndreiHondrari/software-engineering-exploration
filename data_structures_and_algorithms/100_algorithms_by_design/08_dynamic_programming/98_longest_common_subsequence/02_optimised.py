import time

from typing import List, Union


def longest_common_subsequence(
    sequence_1: List[Union[str, int]],
    sequence_2: List[Union[str, int]]
) -> int:

    return 0


def main() -> None:
    tests = [
        ("ABCD", "XABD",),
        ("ABCDEFGHHHHH", "XABDEKKKPPPP",),
        ("ABCDEFGHHHHHZ", "XABDEKKKPPPPZ",),
    ]

    for t in tests:
        sequence_1: List[Union[str, int]] = [c for c in t[0]]
        sequence_2: List[Union[str, int]] = [c for c in t[1]]
        start = time.time()
        lcs = longest_common_subsequence(sequence_1, sequence_2)
        stop = time.time()
        print(f"[{stop - start:.2f} s] LCS for {t[0]} and {t[1]}: {lcs}")


if __name__ == "__main__":
    main()
