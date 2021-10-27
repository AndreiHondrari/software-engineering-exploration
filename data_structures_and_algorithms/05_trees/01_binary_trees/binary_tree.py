from typing import Optional, Any
from dataclasses import dataclass


@dataclass
class Node:
    value: Any
    left: Optional['Node'] = None
    right: Optional['Node'] = None


def node_representation(
    node: 'Node',
    prepend: str = "",
    orientation: str = ""
) -> str:
    node_repr: str = f"{prepend}{orientation} [{node.value}]: {id(node)}\n"

    prepend = "  " if (prepend == "") else (prepend + "  ")

    if (node.left is not None):
        left_repr: str = node_representation(node.left, prepend, "L")
        node_repr += left_repr

    if (node.right is not None):
        right_repr: str = node_representation(node.right, prepend, "R")
        node_repr += right_repr

    return node_repr
