from typing import Optional, Any
from dataclasses import dataclass


@dataclass
class Node:
    value: Any
    left: Optional['Node'] = None
    right: Optional['Node'] = None


def node_representation(
    node: 'Node',
    prepend: str = ""
) -> str:
    node_repr: str = f"{prepend}[{node.value}]\n"

    prepend = "  " if (prepend == "") else (prepend + prepend)

    if (node.left is not None):
        left_repr: str = node_representation(node.left, prepend)
        node_repr += left_repr

    if (node.right is not None):
        right_repr: str = node_representation(node.right, prepend)
        node_repr += right_repr

    return node_repr
