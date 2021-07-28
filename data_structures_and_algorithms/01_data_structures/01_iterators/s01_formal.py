
from typing import List, Generic, TypeVar, Optional

T = TypeVar('T')


class Iterator(Generic[T]):

    @property
    def end_reached(self) -> bool:
        """
        :return: end state of the iterator
        """

        iterable_size = len(self._iterable)
        if (self._index >= iterable_size):
            return True

        return False

    def __init__(self, iterable: List[T]) -> None:
        self._iterable = iterable
        self._index = 0

    def get_value(self) -> Optional[T]:
        """
        :return: value or None
        """

        if self.end_reached:
            return None

        return self._iterable[self._index]

    def set_value(self, value: T) -> bool:
        """
        :return: success state of the operation
        """

        if self.end_reached:
            return False

        self._iterable[self._index] = value
        return True

    def move_next(self) -> bool:
        """
        :return: success state of the operation
        """

        if self.end_reached:
            return False

        self._index += 1
        return True


if __name__ == '__main__':

    print("# ITERATOR demonstration \n")

    some_list: List[int] = [(i + 10 * i) for i in range(1, 10)]

    print("Iterate over elements: ", end="")

    first_iterable = Iterator[int](some_list)
    while not first_iterable.end_reached:
        item = first_iterable.get_value()
        print(item, end=" ")
        first_iterable.move_next()

    print("... DONE")

    print("Iterate over elements changing every third value ", end="")

    second_iterable = Iterator[int](some_list)
    counter = 0
    while not second_iterable.end_reached:
        if counter >= 3:
            second_iterable.set_value(999)
            counter = 0
        second_iterable.move_next()
        counter += 1

    print("... DONE")

    print("Iterate over elements again: ", end="")

    second_iterable = Iterator[int](some_list)
    while not second_iterable.end_reached:
        item = second_iterable.get_value()
        print(item, end=" ")
        second_iterable.move_next()

    print("... DONE")
