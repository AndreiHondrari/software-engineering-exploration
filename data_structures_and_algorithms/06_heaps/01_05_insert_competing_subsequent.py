import functools

from typing import List

from heap import insert


hprint = functools.partial(print, "\n#")


def min_compare(a: int, b: int) -> bool:
    return a < b


def main() -> None:
    hprint("Binary heap")
    heap_array: List[int] = []

    hprint("Insertion")
    values = [50, 30, 20, 10]
    for x in values:
        print("Insert:", x)
        heap_array = insert(heap_array, x, min_compare)
        print("New heap:", heap_array)

    hprint("Result")
    print(heap_array)


if __name__ == "__main__":
    main()
