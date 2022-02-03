import random
import functools
import enum

import dataclasses as dc

from typing import Optional, Any, cast, Tuple, List

import tree_structure


@dc.dataclass(frozen=True)
class TreeError:
    node: 'Node'
    parent: Optional['Node'] = None


@dc.dataclass
class Node(tree_structure.Node):
    left_height: int = 0
    right_height: int = 0

    @property
    def balance_factor(self) -> int:
        return self.left_height - self.right_height

    @property
    def height(self) -> int:
        return max(self.left_height, self.right_height) + 1


add_left_child = functools.partial(tree_structure.add_left_child, klass=Node)
add_right_child = functools.partial(tree_structure.add_right_child, klass=Node)


def validate_tree(
    parent_node: Optional[Node],
    node: Node
) -> List[TreeError]:
    errors = []

    # current node validation
    if node.parent != parent_node:
        errors.append(
            TreeError(
                parent=parent_node,
                node=node,
            )
        )

    # subtree validation
    if node.left is not None:
        errors += validate_tree(node, node.left)

    if node.right is not None:
        errors += validate_tree(node, node.right)

    return errors


def rotate_left(root: Node) -> Node:
    if root.right is None:
        return root

    right_left = root.right.left

    # rewire root and new root
    new_root = root.right
    new_root.parent = root.parent
    new_root.left = root

    root.right = None
    root.parent = new_root

    if right_left is not None:
        right_left.parent = root
        root.right = right_left
        root.right_height = right_left.height
    else:
        root.right_height = 0

    new_root.left_height = root.height

    return new_root


def rotate_right(root: Node) -> Node:
    if root.left is None:
        return root

    left_right = root.left.right

    # rewire root and new root
    new_root = root.left
    new_root.parent = root.parent
    new_root.right = root

    root.left = None
    root.parent = new_root

    if left_right is not None:
        left_right.parent = root
        root.left = left_right
        root.left_height = left_right.height
    else:
        root.left_height = 0

    new_root.right_height = root.height

    return new_root


def rotate_left_right(root: Node) -> Node:
    if root.left is None:
        return root

    root.left = rotate_left(root.left)
    return rotate_right(root)


def rotate_right_left(root: Node) -> Node:
    if root.right is None:
        return root

    root.right = rotate_right(root.right)
    return rotate_left(root)


def balance(node: Node) -> Node:
    new_subroot: Optional[Node] = None

    if abs(node.balance_factor) > 1:
        # handle left inbalance
        if node.balance_factor > 0:
            if cast(Node, node.left).balance_factor >= 0:
                new_subroot = rotate_right(node)
            else:
                new_subroot = rotate_left_right(node)

        # handle right inbalance
        elif node.balance_factor < 0:
            if cast(Node, node.right).balance_factor <= 0:
                new_subroot = rotate_left(node)
            else:
                new_subroot = rotate_right_left(node)

    if new_subroot is None:
        return node

    return new_subroot


def _insert(node: Node, value: Any) -> Tuple[bool, Node]:
    if value == node.value:
        return False, node

    inserted = False

    # handle smaller value
    if value < node.value:
        if node.left is None:
            node.left = Node(parent=node, value=value)
            node.left_height = 1
            inserted = True
        else:
            inserted, new_node = _insert(node.left, value)
            node.left_height = new_node.height

    # handle bigger value
    if value > node.value:
        if node.right is None:
            node.right = Node(parent=node, value=value)
            node.right_height = 1
            inserted = True
        else:
            inserted, new_node = _insert(node.right, value)
            node.right_height = new_node.height

    # determine balance status
    if inserted:
        old_parent = node.parent
        node.parent = None

        new_subroot = balance(node)
        new_subroot.parent = old_parent

        if old_parent is not None:
            is_left = old_parent.left is node
            if is_left:
                old_parent.left = new_subroot
            else:
                old_parent.right = new_subroot

        return True, new_subroot

    return False, node


def insert(root: Optional[Node], value: Any) -> Node:
    # just create the root if it doesn't exist
    if root is None:
        return Node(value=value)

    _, root = _insert(root, value)

    return root
