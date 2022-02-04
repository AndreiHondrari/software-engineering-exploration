import functools

from typing import List

from heap import insert


hprint = functools.partial(print, "\n#")


def min_compare(a: int, b: int) -> bool:
    return a < b


def main() -> None:
    hprint("Binary heap")
    heap_array: List[int] = []

    heap_array = insert(heap_array, 50, min_compare)

    hprint("Result")
    print(heap_array)


if __name__ == "__main__":
    main()
