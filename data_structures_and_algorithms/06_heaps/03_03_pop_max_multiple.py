import functools

from typing import List

from heap import heapify, pop


hprint = functools.partial(print, "\n#")


def max_compare(a: int, b: int) -> bool:
    return a > b


def main() -> None:
    hprint("Binary heap")
    heap_array: List[int] = []

    hprint("Heapify")
    values = [35, 33, 42, 10, 14, 19, 27, 44, 26, 31]
    print("Input:", values)
    heap_array = heapify(values, max_compare)
    print("Heapified:", heap_array)

    hprint("Max value extraction")
    for i in range(len(heap_array)):
        max_value, heap_array = pop(heap_array, max_compare)
        print("Max:", max_value)
        print("Last heap:", heap_array)


if __name__ == "__main__":
    main()
