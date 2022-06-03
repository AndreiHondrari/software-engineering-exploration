from collections import defaultdict, deque

from typing import Deque, Set, Dict, Tuple


def first_non_rep(text: str) -> int:

    # keeps the order of appearence of letters
    first_appearence_queue: Deque[Tuple[int, str]] = deque()

    # keep the status of the first appearence
    # if it is in this set then it was already
    # encountered
    appearence_set: Set[str] = set()

    # determines if a letter is a duplicate
    duplicates: Dict[str, bool] = defaultdict(bool)

    # evaluate the letters
    for i, char in enumerate(text):
        if char in appearence_set:
            duplicates[char] = True
        else:
            appearence_set.add(char)
            first_appearence_queue.append((i, char))

    # find the first non-repeating character
    while len(first_appearence_queue) > 0:
        # we get first char in line
        char_index, char = first_appearence_queue.popleft()

        # determine if char is unique
        if not duplicates[char]:
            return char_index

    return -1


def main() -> None:
    tests = [
        "magnificus",
        "aabcc",
        "aabbc",
        "xyz"
    ]

    for t in tests:
        k = first_non_rep(t)
        print(k, t)


if __name__ == "__main__":
    main()
