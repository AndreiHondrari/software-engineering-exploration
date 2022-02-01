from dataclasses import dataclass
from typing import Optional, List, Any


class NotLinkedListChild(Exception):
    pass


@dataclass
class Node:
    value: Any
    parent: 'LinkedList'
    prev: Optional['Node'] = None
    next: Optional['Node'] = None


@dataclass
class LinkedList:
    head: Optional[Node] = None
    tail: Optional[Node] = None

    def __str__(self) -> str:
        values: List[str] = []
        p = self.head
        while (p is not None):
            values.append(str(p.value))
            p = p.next

        return " -> ".join(values)

    def insert_at_end(self, new_value: Any) -> Node:
        new_node = Node(value=new_value, parent=self)

        if (self.tail is None):
            self.head = new_node
            new_node.prev = None
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        new_node.next = None

        return new_node

    def remove(self, node: Node) -> None:
        if node.parent != self:
            raise NotLinkedListChild

        prev: Optional[Node] = node.prev
        next: Optional[Node] = node.next

        if prev is None:
            self.head = next
        else:
            prev.next = next

        if next is None:
            self.tail = prev
        else:
            next.prev = prev
