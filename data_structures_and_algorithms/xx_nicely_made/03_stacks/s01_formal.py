from typing import Generic, TypeVar, Optional, cast

T = TypeVar('T')


class Item(Generic[T]):

    @property
    def value(self) -> T:
        return self._value

    @property
    def under_item(self) -> Optional['Item[T]']:
        return self._under_item

    @under_item.setter
    def under_item(self, item: Optional['Item[T]']) -> None:
        self._under_item = item

    def __init__(
        self,
        value: T,
        under_item: Optional['Item[T]'] = None
    ) -> None:
        self._under_item: Optional['Item[T]'] = (  # type: ignore[no-redef]
            under_item
        )

        self._value = value


class Stack(Generic[T]):

    @property
    def is_full(self) -> bool:
        return self._current_size >= self._max_items

    @property
    def is_empty(self) -> bool:
        return self._current_size == 0

    @property
    def size(self) -> int:
        return self._current_size

    @property
    def top(self) -> Optional[T]:
        if self._top is None:
            return None

        return self._top.value

    def __init__(self, max_size: int):
        self._max_items = max_size
        self._current_size = 0
        self._top: Optional[Item[T]] = None

    def peek(self, index: int) -> Optional[T]:
        if index >= self._current_size:
            return None

        item = self._top
        for i in range(index):
            item = cast(Item[T], item).under_item

        return cast(Item[T], item).value

    def push(self, value: T) -> bool:
        """
        Inserts value on top of the stack.

        :return: Insertion success state. Fails if stack is full.
        """

        if self.is_full:
            return False

        if self._top is None:
            self._top = Item[T](value)
        else:
            previous_top = self._top
            self._top = Item[T](value, previous_top)

        self._current_size += 1
        return True

    def pop(self) -> Optional[T]:
        """
        Returns the top most item or nothing if the stack is empty
        """

        if self.is_empty:
            return None

        self._current_size -= 1
        top_item = self._top
        self._top = cast(Item[T], self._top).under_item
        return cast(Item[T], top_item).value


def printout(stack: Stack[T], name: str) -> None:
    print(f"[{name}] stack printout: ", end="")
    for i in range(stack.size):
        val = stack.peek(i)
        print(val, end=" ")
    print("...done")


if __name__ == '__main__':

    MAX_SIZE = 5

    stack = Stack[int](MAX_SIZE)

    print("Insert some things up to max")
    for i in range(1, MAX_SIZE + 1):
        stack.push(i + 10 * i)

    printout(stack, "FIRST")

    print("Push one extra", end="")
    result = stack.push(9999)
    print(f"... result: {result}")

    printout(stack, "SECOND")

    print("Pop one", end="")
    value = stack.pop()
    print(f"... value: {value}")

    print("Pop another", end="")
    value = stack.pop()
    print(f"... value: {value}")

    printout(stack, "THIRD")

    print("Pop multiple: ", end="")
    print(stack.pop(), end=" ")
    print(stack.pop(), end=" ")
    print(stack.pop(), end=" ")
    print(stack.pop(), end=" ")  # should yield None as there is nothing left
    print("... done")

    printout(stack, "FOURTH")

    print("Push a last time", end="")
    result = stack.push(9999)
    print(f"... result: {result}")

    printout(stack, "FIFTH")
