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


class Dequeue(Generic[T]):

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

    def push_back(self, value: T) -> bool:
        """
        Enqueue normally at the tail of the queue
        (analogy - people get in a line)
        """

        if self.is_full:
            return False

        # if no items in the queue, just insert it
        if self.is_empty:
            self._back = Item[T](value)
            self._front = self._back

        # if items exists in the queue, just insert at the back
        else:
            new_item = Item[T](value, next_item=self._back)
            cast(Item[T], self._back).previous_item = new_item
            self._back = new_item

        self._current_size += 1
        return True

    def push_front(self, value: T) -> bool:
        """
        Enqueueing in front of all others
        (analogy - someone forcefully goes in
        front of everybody else in a line)
        """

        # if no items in the queue, just insert it
        if self.is_empty:
            self._back = Item[T](value)
            self._front = self._back

        # if items exists in the queue, just insert at the front
        else:
            front: Item[T] = cast(Item[T], self._front)
            new_item = Item[T](value)
            front.next_item = new_item
            self._front = front.next_item

        if self.is_full:
            return False

        self._current_size += 1
        return True

    def pop_back(self) -> Optional[T]:
        """
        Dequeue from the back of the queue
        (analogy - someone from the back of the queue is tired of waiting
        in the line and leaves)
        """

        if self.is_empty:
            return None

        # memorize the current back
        item: Item[T] = cast(Item[T], self._back)

        # the new back will be the one after the current back
        self._back = cast(Item[T], self._back).next_item
        if self._back is not None:
            self._back.previous_item = None

        self._current_size -= 1
        return item.value

    def pop_front(self) -> Optional[T]:
        """
        Dequeue normally from the head of the queue
        (analogy - the person next in line gets served)
        """

        if self.is_empty:
            return None

        # memorize the current front
        item: Item[T] = cast(Item[T], self._front)

        # the new front will be the next in line
        # (meaning the item located in the rear of the current front item)
        self._front = cast(Item[T], self._front).previous_item
        if self._front is not None:
            self._front.next_item = None

        self._current_size -= 1
        return item.value


def printout(dequeue: Dequeue[T], name: str) -> None:
    print(f"[{name}] dequeue printout: ", end="")
    for i in range(dequeue.size):
        val = dequeue.peek(i)
        print(val, end=" ")
    print("... done")


if __name__ == '__main__':

    MAX_SIZE = 5

    dequeue = Dequeue[int](MAX_SIZE)

    print("Push back some things up to max")
    for i in range(1, MAX_SIZE + 1):
        dequeue.push_back(i + 10 * i)

    printout(dequeue, "FIRST")

    print("Push back one extra", end="")
    result = dequeue.push_back(9999)
    print(f"... result: {result}")

    printout(dequeue, "SECOND")

    print("Pop one from the back", end="")
    value = dequeue.pop_back()
    print(f"... value: {value}")

    print("Pop one from the front", end="")
    value = dequeue.pop_front()
    print(f"... value: {value}")

    printout(dequeue, "THIRD")

    print("Pop multiple: ", end="")
    print(dequeue.pop_front(), end=" ")
    print(dequeue.pop_back(), end=" ")
    print(dequeue.pop_front(), end=" ")
    print(dequeue.pop_back(), end=" ")  # should yield None (nothing left)
    print("... done")

    printout(dequeue, "FOURTH")

    print("Push a last time", end="")
    result = dequeue.push_front(9999)
    print(f"... result: {result}")

    printout(dequeue, "FIFTH")
