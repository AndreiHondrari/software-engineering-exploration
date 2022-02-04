import functools

import dataclasses as dc
from typing import Optional, Tuple, Callable

import tree_structure


@dc.dataclass
class Node(tree_structure.Node):
    priority: int = 0


add_left_child = functools.partial(tree_structure.add_left_child, klass=Node)
add_right_child = functools.partial(tree_structure.add_right_child, klass=Node)


def swap_parent_child(parent: Node, child: Node) -> Node:
    """
    :return: new parent
    """
    assert parent.left is child or parent.right is child
    assert child.parent is parent

    parent_left = parent.left
    parent_right = parent.right

    child_left = child.left
    child_right = child.right

    is_child_left: bool = parent.left is child

    # rewire parents
    if parent.parent is not None:
        is_parent_left: bool = parent.parent.left is parent
        if is_parent_left:
            parent.parent.left = child
        else:
            parent.parent.right = child

    child.parent = parent.parent
    parent.parent = child

    if child_left is not None:
        child_left.parent = parent

    if child_right is not None:
        child_right.parent = parent

    # rewire left/right
    parent.left = child_left
    parent.right = child_right

    if is_child_left:
        child.left = parent
        child.right = parent_right
        if child.right is not None:
            child.right.parent = child
    else:
        child.left = parent_left
        child.right = parent
        if child.left is not None:
            child.left.parent = child

    return child
