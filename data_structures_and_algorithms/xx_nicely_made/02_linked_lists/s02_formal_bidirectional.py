
from typing import Generic, TypeVar, Optional, cast

T = TypeVar('T')


class Node(Generic[T]):

    def __init__(
        self,
        value: T,
        previous_node: Optional['Node[T]'] = None,
        next_node: Optional['Node[T]'] = None
    ) -> None:
        self._value: T = value
        self._previous_node = previous_node
        self._next_node = next_node

    @property
    def value(self) -> T:
        return self._value

    @property
    def previous_node(self) -> Optional['Node[T]']:
        return self._previous_node

    @previous_node.setter
    def previous_node(self, node: 'Optional[Node[T]]') -> None:
        self._previous_node = node

    @property
    def next_node(self) -> Optional['Node[T]']:
        return self._next_node

    @next_node.setter
    def next_node(self, node: 'Optional[Node[T]]') -> None:
        self._next_node = node


class LinkedList(Generic[T]):

    @property
    def is_empty(self) -> bool:
        return self._head is None

    @property
    def head(self) -> Optional[Node[T]]:
        return self._head

    @property
    def tail(self) -> Optional[Node[T]]:
        return self._tail

    @property
    def size(self) -> int:
        return self._size

    def __init__(self) -> None:
        self._head: Optional[Node[T]] = None
        self._tail: Optional[Node[T]] = None
        self._size: int = 0

    def __len__(self) -> int:
        return self._size

    def insert(self, value: T, index: Optional[int] = None) -> None:
        new_node = Node(value)

        # insertion in a specific index
        # insertion at the end
        if index is None or index is not None and index >= self._size:
            if self._tail is None:
                self._head = new_node
                self._tail = self._head
            else:
                self._tail.next_node = new_node
                new_node._previous_node = self._tail
                self._tail = new_node

        else:
            node: Node[T] = cast(Node[T], self._head)

            # reach the node
            for i in range(index):
                node = cast(Node[T], node.next_node)

            if node.previous_node is not None:
                node.previous_node.next_node = new_node
            new_node.next_node = node

        self._size += 1

    def get(self, index: int) -> Optional[T]:
        if index >= self._size:
            return None

        current: Node[T] = cast(Node[T], self._head)

        # reach the node
        for i in range(index):
            current = cast(Node[T], current.next_node)

        return current.value

    def remove(self, index: int) -> bool:
        """
        :return: Removal success status. Fails if index is out of range.
        """

        if index >= self._size:
            return False

        node: Node[T] = cast(Node[T], self._head)

        # reach the node
        for i in range(index):
            node = cast(Node[T], node.next_node)

        # perform the removal
        if node.previous_node is None:
            self._head = node.next_node
        else:
            node.previous_node.next_node = node.next_node

        self._size -= 1
        return True


class ListIterator(Generic[T]):

    @property
    def end_reached(self) -> bool:
        """
        :return: end state of the iterator
        """

        iterable_size = len(self._linked_list)
        if (self._index >= iterable_size):
            return True

        return False

    def __init__(self, linked_list: LinkedList[T]) -> None:
        self._linked_list = linked_list
        self._current_node = self._linked_list.head
        self._index = 0

    def get_value(self) -> Optional[T]:
        """
        :return: value or None
        """

        if self.end_reached:
            return None

        return cast(Node[T], self._current_node).value

    def move_next(self) -> bool:
        """
        :return: success state of the operation
        """

        if self.end_reached:
            return False

        self._current_node = cast(Node[T], self._current_node).next_node
        self._index += 1
        return True


def printout(linked_list: LinkedList[T], name: str) -> None:
    print(f"[{name}] iteration over all: ", end="")
    iterator = ListIterator[T](linked_list)
    while not iterator.end_reached:
        print(iterator.get_value(), end=" ")
        iterator.move_next()
    print("... done")


if __name__ == '__main__':
    linked_list = LinkedList[int]()

    linked_list.insert(11)
    linked_list.insert(22)
    linked_list.insert(33)
    linked_list.insert(44)
    linked_list.insert(55)

    printout(linked_list, "FIRST")

    print(f"Third item: {linked_list.get(2)}")

    print("Insert on the second position")
    linked_list.insert(99999, 1)
    printout(linked_list, "SECOND")

    print("Remove the fourth")
    linked_list.remove(3)

    printout(linked_list, "THIRD")

    print("Multiple removals")
    linked_list.remove(0)
    linked_list.remove(0)
    linked_list.remove(0)
    linked_list.remove(0)
    linked_list.remove(0)
    linked_list.remove(0)

    printout(linked_list, "FOURTH")
