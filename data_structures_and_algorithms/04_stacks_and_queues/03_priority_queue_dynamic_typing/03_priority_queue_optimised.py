import random
import functools
import time
import dataclasses

from collections import namedtuple, defaultdict
from typing import Set, List, Dict, Optional, cast

from linked_list import LinkedList, Node

hprint = functools.partial(print, "\n#")

PQElement = namedtuple(
    "PQElement",
    ['value', 'priority']
)


@dataclasses.dataclass
class PriorityQueue:
    max_size: int
    current_size: int = 0
    elements: LinkedList = LinkedList()
    priorities: Set[int] = dataclasses.field(default_factory=set)
    priority_map: Dict[int, List[Node]] = dataclasses.field(
        default_factory=lambda: defaultdict(list)
    )

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
        new_node = self.elements.insert_at_end(new_element)
        self.current_size += 1
        self.priorities.add(priority)
        self.priority_map[priority].append(new_node)
        return new_element

    def pull(self) -> Optional[PQElement]:
        if self.elements.head is None:
            return None

        # get highest priority level available
        max_priority = max(self.priorities)

        # get a node for that priority level
        high_node = self.priority_map[max_priority].pop()
        if len(self.priority_map[max_priority]) == 0:
            self.priorities.remove(max_priority)

        # remove the node from the list of elements
        self.elements.remove(high_node)

        # return high element
        high_element: PQElement = cast(PQElement, high_node.value)

        return high_element


if __name__ == '__main__':
    hprint("Optimised Priority Queue with large collections")

    QUERY_SIZE: int = 5

    SIZE: int = 50_000
    pq = PriorityQueue(max_size=SIZE)

    print("Insert random values in the priority queue ...")
    elements = []
    for _ in range(SIZE):
        new_element = pq.insert(
            new_value=random.randint(1_000, 10_000),
            priority=random.randint(0, 100)
        )
        elements.append(new_element)

    print("length:", len(pq))

    hprint(f"first {QUERY_SIZE} elements")
    for x in elements[:QUERY_SIZE]:
        print(x)

    hprint(f"last {QUERY_SIZE} elements")
    for x in elements[-QUERY_SIZE:]:
        print(x)

    del elements

    hprint("Pull them by priority")
    results = []

    start = time.time()

    for _ in range(len(pq)):
        x: Optional[PQElement] = pq.pull()
        results.append(x)

    hprint(f"first {QUERY_SIZE} results")
    for x in results[:QUERY_SIZE]:
        print(x)

    hprint(f"last {QUERY_SIZE} results")
    for x in results[-QUERY_SIZE:]:
        print(x)

    stop = time.time()

    print(f"time spent pulling: {stop-start:.2f}s")
    print("result length:", len(results))
