from typing import Any, List
import dataclasses as dc


@dc.dataclass
class Node:
    value: Any
    children: List['Node'] = dc.field(default_factory=list)

    @staticmethod
    def _node_representation(
        node: 'Node',
        prepend: str = ""
    ) -> str:
        node_repr: str = f"{prepend}[{node.value}]\n"

        prepend = "  " if (prepend == "") else (prepend + prepend)

        for child in node.children:
            child_repr: str = Node._node_representation(child, prepend)
            node_repr += child_repr

        return node_repr

    def __str__(self) -> str:
        return Node._node_representation(self)


if __name__ == '__main__':

    # level 2 children - incidentally leafs
    n3: Node = Node(44)
    n4: Node = Node(55)
    n5: Node = Node(66)
    n6: Node = Node(77)
    n7: Node = Node(88)

    # level 1 children
    n1: Node = Node(22, children=[n3, n4, n5])
    n2: Node = Node(33, children=[n6, n7])

    # root node
    n0: Node = Node(11, children=[n1, n2])

    print(n0)
