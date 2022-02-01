import random
import functools
import time

from collections import namedtuple
from dataclasses import dataclass
from typing import Optional, cast

from linked_list import LinkedList, Node

hprint = functools.partial(print, "\n#")


PQElement = namedtuple(
    "PQElement",
    ['value', 'priority']
)


@dataclass
class PriorityQueue:
    max_size: int
    current_size: int = 0
    elements: LinkedList = LinkedList()

    def __len__(self) -> int:
        return self.current_size

    def __str__(self) -> str:
        return str(self.elements)

    def insert(self, new_value: int, priority: int) -> Optional[PQElement]:
        if self.current_size == self.max_size:
            return None

        new_element = PQElement(
            value=new_value,
            priority=priority
        )
        self.elements.insert_at_end(new_element)
        self.current_size += 1
        return new_element

    def pull(self) -> Optional[PQElement]:
        if self.elements.head is None:
            return None

        highest_node: Node = self.elements.head
        highest: PQElement = cast(PQElement, highest_node.value)

        p: Optional[Node] = self.elements.head

        while p is not None:
            if highest.priority < p.value.priority:
                highest_node = p
                highest = highest_node.value

            p = p.next

        self.elements.remove(highest_node)
        self.current_size -= 1
        return highest


if __name__ == '__main__':
    hprint("Priority queue with large collections")
    SIZE: int = 5_000
    pq = PriorityQueue(max_size=SIZE)

    print("Insert random values in the priority queue ...")
    for _ in range(SIZE):
        pq.insert(
            new_value=random.randint(1_000, 10_000),
            priority=random.randint(0, 100)
        )

    print(len(pq))

    hprint("Pull them by priority")
    result = []
    start = time.time()
    for _ in range(len(pq)):
        x: Optional[PQElement] = pq.pull()
        result.append(x)
    stop = time.time()

    print(f"time spent pulling: {stop-start:.2f}s")
    print("result length:", len(result))
