from typing import Generic, TypeVar, Optional, cast

T = TypeVar('T')


class Item(Generic[T]):

    @property
    def value(self) -> T:
        return self._value

    @property
    def previous_item(self) -> Optional['Item[T]']:
        return self._previous_item

    @previous_item.setter
    def previous_item(self, item: Optional['Item[T]']) -> None:
        self._previous_item = item

    @property
    def next_item(self) -> Optional['Item[T]']:
        return self._next_item

    @next_item.setter
    def next_item(self, item: Optional['Item[T]']) -> None:
        self._next_item = item

    def __init__(
        self,
        value: T,
        next_item: Optional['Item[T]'] = None,
        previous_item: Optional['Item[T]'] = None
    ) -> None:

        self._previous_item: Optional['Item[T]'] = (  # type: ignore[no-redef]
            previous_item
        )

        self._next_item: Optional['Item[T]'] = (  # type: ignore[no-redef]
            next_item
        )

        self._value = value


class Queue(Generic[T]):

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
    def back(self) -> Optional[T]:
        if self._back is None:
            return None

        return self._back.value

    @property
    def front(self) -> Optional[T]:
        if self._front is None:
            return None

        return self._front.value

    def __init__(self, max_size: int):
        self._max_items = max_size
        self._current_size = 0
        self._back: Optional[Item[T]] = None
        self._front: Optional[Item[T]] = None

    def peek(self, index: int) -> Optional[T]:
        if index >= self._current_size:
            return None

        item = self._front
        for i in range(index):
            item = cast(Item[T], item).previous_item

        return cast(Item[T], item).value

    def enqueue(self, value: T) -> bool:
        if self.is_full:
            return False

        # make the new item as back and front
        if self.is_empty:
            self._back = Item[T](value)
            self._front = self._back

        # or make the new item as the new back
        else:
            new_item = Item[T](value, next_item=self._back)
            cast(Item[T], self._back).previous_item = new_item
            self._back = new_item

        self._current_size += 1
        return True

    def dequeue(self) -> Optional[T]:
        if self.is_empty:
            return None

        item: Item[T] = cast(Item[T], self._front)

        # make the next in line (previous item) as the new front
        self._front = cast(Item[T], self._front).previous_item
        if self._front is not None:
            self._front.next_item = None

        self._current_size -= 1
        return item.value


def printout(queue: Queue[T], name: str) -> None:
    print(f"[{name}] queue printout: ", end="")
    for i in range(queue.size):
        val = queue.peek(i)
        print(val, end=" ")
    print("... done")


if __name__ == '__main__':

    MAX_SIZE = 5

    queue = Queue[int](MAX_SIZE)

    print("Insert some things up to max")
    for i in range(1, MAX_SIZE + 1):
        queue.enqueue(i + 10 * i)

    printout(queue, "FIRST")

    print("Push one extra", end="")
    result = queue.enqueue(9999)
    print(f"... result: {result}")

    printout(queue, "SECOND")

    print("Pop one", end="")
    value = queue.dequeue()
    print(f"... value: {value}")

    print("Pop another", end="")
    value = queue.dequeue()
    print(f"... value: {value}")

    printout(queue, "THIRD")

    print("Pop multiple: ", end="")
    print(queue.dequeue(), end=" ")
    print(queue.dequeue(), end=" ")
    print(queue.dequeue(), end=" ")
    print(queue.dequeue(), end=" ")  # should yield None (nothing left)
    print("... done")

    printout(queue, "FOURTH")

    print("Push a last time", end="")
    result = queue.enqueue(9999)
    print(f"... result: {result}")

    printout(queue, "FIFTH")
