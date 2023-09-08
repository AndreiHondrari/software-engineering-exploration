import copy
from collections import deque, namedtuple

from typing import Union, List, Deque

RootSequence = namedtuple('RootSequence', ['sequence', 'last_position'])


def generate_subsequences(
    sequence: List[Union[str, int]]
) -> List[List[Union[str, int]]]:
    """
    Generate subsequences

    time complexity analysis:
    O(n) + O(n^2) = O(n^2)

    space complexity analysis:
    incidentally it is the same as the time complexity
    because for each root sequence another set of root sequences is born
    hence O(n^2)
    """
    subsequences: List[List[Union[str, int]]] = []

    root_sequences: Deque[RootSequence] = deque()

    # initial push - O(n)
    for index, item in enumerate(sequence):
        new_root_sequence = RootSequence(sequence=[item], last_position=index)
        root_sequences.append(new_root_sequence)

    # generate based on root sequences
    # and create new root_sequences on the fly
    while len(root_sequences) > 0:
        root_sequence = root_sequences.popleft()
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
    sequence_1: List[Union[str, int]],
    sequence_2: List[Union[str, int]]
) -> List[List[Union[str, int]]]:
    """
    time complexity analysis:
    O(n^2) + O(m^2) = O(max(n, m) ^ 2)

    Omega = O because no matter how the data is,
    generate_subsequences still takes O(max(n, m) ^ 2)
    """
    common_subsequences: List[List[Union[str, int]]] = []

    subsequences_1 = generate_subsequences(sequence_1)  # O(n^2)
    subsequences_2 = generate_subsequences(sequence_2)  # O(m^2)

    # O(k^2) which coincidentally is O(n * m)
    for seq1 in subsequences_1:
        for seq2 in subsequences_2:
            if seq1 == seq2:
                common_subsequences.append(seq1)

    return common_subsequences


def main() -> None:
    tests = [
        ("ABCD", "XABD",),
    ]

    for t in tests:
        sequence_1: List[Union[str, int]] = [c for c in t[0]]
        sequence_2: List[Union[str, int]] = [c for c in t[1]]
        common_subsequences = find_common_subsequences(sequence_1, sequence_2)

        print(f" \n# Subsequences for {t[0]} and {t[1]}")
        for sequence in common_subsequences:
            print(sequence)


if __name__ == "__main__":
    main()
