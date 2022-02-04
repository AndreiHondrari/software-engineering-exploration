
import copy
from typing import List, Tuple, Callable, Optional


def get_parent(reference_index: int) -> int:
    if reference_index % 2 == 0:
        return (reference_index - 2) // 2
    else:
        return (reference_index - 1) // 2


def get_left(parent_index: int) -> int:
    return parent_index * 2 + 1


def get_right(parent_index: int) -> int:
    return parent_index * 2 + 2


def insert(
    heap_array: List[int],
    new_value: int,
    compare_func: Callable[[int, int], bool]
) -> List[int]:
    """
    :return: Resulting heap array
    """
    new_heap = copy.copy(heap_array)

    new_heap.append(new_value)

    reference_index = len(new_heap) - 1

    # if it's the root we don't do anything else
    if reference_index == 0:
        return new_heap

    # compare the new child with the parent and swap if necessary

    while reference_index > 0:
        parent_index = get_parent(reference_index)
        if not compare_func(new_heap[parent_index], new_heap[reference_index]):
            tmp = new_heap[parent_index]
            new_heap[parent_index] = new_heap[reference_index]
            new_heap[reference_index] = tmp

        reference_index = parent_index

    return new_heap


def heapify(
    input_array: List[int],
    compare_func: Callable[[int, int], bool] = lambda a, b: a < b
) -> List[int]:
    """
    :return: Binary heap of the input array
    """

    new_heap: List[int] = []

    for x in input_array:
        new_heap = insert(new_heap, x, compare_func)

    return new_heap


def get_extreme(heap: List[int]) -> Optional[int]:
    return None if len(heap) == 0 else heap[0]


def pop(
    heap: List[int],
    compare_func: Callable[[int, int], bool] = lambda a, b: a < b
) -> Tuple[Optional[int], List[int]]:
    new_heap = copy.copy(heap)

    if len(new_heap) == 0:
        return None, []

    extreme = new_heap[0]
    last_index = len(new_heap) - 1
    new_heap[0] = new_heap[last_index]
    del new_heap[last_index]

    last_index -= 1

    reference_index = 0
    while reference_index < last_index:
        left_index = get_left(reference_index)
        right_index = get_right(reference_index)

        if (
            right_index <= last_index and
            not compare_func(new_heap[left_index], new_heap[right_index])
        ):
            child_index = right_index
        else:
            child_index = left_index

        if child_index > last_index:
            break

        if not compare_func(new_heap[reference_index], new_heap[child_index]):
            tmp = new_heap[reference_index]
            new_heap[reference_index] = new_heap[child_index]
            new_heap[child_index] = tmp

        reference_index = child_index

    return extreme, new_heap
