import functools

from typing import List

from heap import heapify, pop


hprint = functools.partial(print, "\n#")


def min_compare(a: int, b: int) -> bool:
    return a < b


def main() -> None:
    hprint("Binary heap")
    heap_array: List[int] = []

    hprint("Heapify")
    values = [35, 33, 42, 10, 14, 19, 27, 44, 26, 31]
    print("Input:", values)
    heap_array = heapify(values, min_compare)
    print("Heapified:", heap_array)

    hprint("Min value extraction")
    min_value, heap_array = pop(heap_array)
    print("Min:", min_value)
    print("Last heap:", heap_array)


if __name__ == "__main__":
    main()
