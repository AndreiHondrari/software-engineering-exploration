"""
Find the longest common subsequence - NAIVE

Steps:
* generate the set of all subsequences for sequence A
* generate the set of all subsequences for sequence B
* brute force compare the subsequences to find the common subsequences
* brute force compare the common subsequences to find the longest one
"""

import copy
import time
from collections import deque, namedtuple

from typing import List, Deque

Character = str

RootSequence = namedtuple('RootSequence', ['sequence', 'last_position'])


def generate_subsequences(
    sequence: List[Character]
) -> List[List[Character]]:
    """
    Generate subsequences

    Generates combinations of items from the sequence, in original order.

    time complexity analysis:
    O(n) + O(c^n)

    space complexity analysis:
    incidentally it is the same as the time complexity
    because for each root sequence another set of root sequences is born
    hence O(n^2)
    """

    # the resulting subsequences
    subsequences: List[List[Character]] = []

    # the sequencees to be used for generation of subsequences
    root_sequences: Deque[RootSequence] = deque()

    # initial push - O(n)
    for index, item in enumerate(sequence):
        new_root_sequence = RootSequence(sequence=[item], last_position=index)
        root_sequences.append(new_root_sequence)

    # generate based on root sequences
    # and create new root_sequences on the fly
    while len(root_sequences) > 0:
        root_sequence: RootSequence = root_sequences.popleft()
        subsequences.append(root_sequence.sequence)

        for i in range(root_sequence.last_position + 1, len(sequence)):
            new_sequence = copy.copy(root_sequence.sequence)
            new_sequence.append(sequence[i])

            new_root_sequence = RootSequence(
                sequence=new_sequence,
                last_position=i
            )
            root_sequences.append(new_root_sequence)

    return subsequences


def find_common_subsequences(
    sequence_1: List[Character],
    sequence_2: List[Character]
) -> List[List[Character]]:
    """
    time complexity analysis:
    O(a^n) + O(b^m) = O(max(a^n, b^m))

    Omega = O because no matter how the data is,
    generate_subsequences still takes O(max(a^n, b^m))
    """
    common_subsequences: List[List[Character]] = []

    subsequences_1 = generate_subsequences(sequence_1)  # O(n^2)
    subsequences_2 = generate_subsequences(sequence_2)  # O(m^2)

    # O(k^2) which coincidentally is O(n * m)
    for seq1 in subsequences_1:
        for seq2 in subsequences_2:
            if seq1 == seq2:
                common_subsequences.append(seq1)

    return common_subsequences


def longest_common_subsequence(
    sequence_1: List[Character],
    sequence_2: List[Character]
) -> List[Character]:
    """
    # O(max(a^n, b^m))
    """

    longest_common_subsequence: List[Character] = []

    # O(max(a^n, b^m))
    common_subsequences: List[List[Character]] = find_common_subsequences(
        sequence_1,
        sequence_2
    )

    max_size = 0

    # O(max(a^n, b^m) / 2) = O(max(a^n, b^m))
    for seq in common_subsequences:
        new_max_size = max(max_size, len(seq))

        if new_max_size != max_size:
            max_size = new_max_size
            longest_common_subsequence = seq

    return longest_common_subsequence


def main() -> None:
    tests = [
        ("XA", "AA",),
        ("AA", "XA",),
        ("ABCD", "XABD",),
        ("XABD", "ABCD",),
        ("ADEFIJK", "FDEIK",),
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
