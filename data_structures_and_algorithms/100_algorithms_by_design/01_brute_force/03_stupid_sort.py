"""

"""
import random
import functools
import copy

from typing import List, Tuple

hprint = functools.partial(print, "\n#")


def _generate_permutations(
    values: List[int],
) -> List[List[int]]:
    permutations = [values]

    if len(values) == 1:
        return permutations

    for i in range(0, len(values)):
        permutation = copy.copy(values)

        if i > 0:
            permutation[0] = values[i]
            permutation[i] = values[0]

        sub_permutations = _generate_permutations(permutation[1:])

        for subperm in sub_permutations:
            permutations.append([permutation[0]] + subperm)

    return permutations


def generate_permutations(values: List[int]) -> Tuple[Tuple[int, ...], ...]:
    if len(values) == 0:
        return tuple()

    return tuple(map(lambda x: tuple(x), _generate_permutations(values)))


def brute_sort(unsorted_items: List[int]) -> Tuple[int, ...]:
    """
    Stupid sort

    - Generate all combinations
    - Iterate through all the combinations and determine if all the values are
    in order -> memorize the ones that are
    """

    permutations: Tuple[
        Tuple[int, ...], ...
    ] = generate_permutations(unsorted_items)

    for permutation in permutations:
        is_ordered = True
        for i in range(len(permutation) - 1):
            if permutation[i] > permutation[i+1]:
                is_ordered = False

        if is_ordered:
            return tuple(permutation)

    return tuple()


def main() -> None:
    values = [random.randint(1, 100) for _ in range(9)]

    hprint("Unsorted values")
    print(values)

    hprint("Sorted values")
    sorted_values = brute_sort(values)
    print(sorted_values)


if __name__ == "__main__":
    main()
