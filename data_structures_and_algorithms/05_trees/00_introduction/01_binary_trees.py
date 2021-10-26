from typing import Optional, Any
from dataclasses import dataclass


@dataclass
class Node:
    value: Any
    left: Optional['Node'] = None
    right: Optional['Node'] = None

    @staticmethod
    def _node_representation(
        node: 'Node',
        prepend: str = ""
    ) -> str:
        node_repr: str = f"{prepend}[{node.value}]\n"

        prepend = "  " if (prepend == "") else (prepend + prepend)

        if (node.left is not None):
            left_repr: str = Node._node_representation(node.left, prepend)
            node_repr += left_repr

        if (node.right is not None):
            right_repr: str = Node._node_representation(node.right, prepend)
            node_repr += right_repr

        return node_repr

    def __str__(self) -> str:
        return Node._node_representation(self)


if __name__ == '__main__':

    # level 2 children - incidentally leafs
    n3: Node = Node(44)
    n4: Node = Node(55)
    n5: Node = Node(66)
    n6: Node = Node(77)

    # level 1 children
    n2: Node = Node(33, left=n5, right=n6)
    n1: Node = Node(22, left=n3, right=n4)

    # root node
    n0: Node = Node(11, left=n1, right=n2)

    print(n0)
