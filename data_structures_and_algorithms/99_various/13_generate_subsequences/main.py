import copy
from collections import deque, namedtuple

from typing import Union, List, Deque

RootSequence = namedtuple('RootSequence', ['sequence', 'last_position'])


def generate_subsequences(
    sequence: List[Union[str, int]]
) -> List[List[Union[str, int]]]:
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


def main() -> None:
    tests = ["ABCD", "WXYZ"]

    for t in tests:
        subsequences = generate_subsequences([c for c in t])
        print(f" \n# Subsequences for {t}")
        for seq in subsequences:
            print(seq)


if __name__ == "__main__":
    main()
