import random
import dataclasses as dc
from typing import Optional, Any


@dc.dataclass
class Node:
    value: Any
    parent: Optional['Node'] = dc.field(default=None, repr=False)

    left: Optional['Node'] = dc.field(default=None, repr=False)
    right: Optional['Node'] = dc.field(default=None, repr=False)

    left_height: int = 0
    right_height: int = 0

    @property
    def balance_factor(self) -> int:
        return self.left_height - self.right_height

    # for display purposes
    control_id: int = dc.field(
        init=False,
        repr=False,
        default_factory=lambda: random.randint(0, 10_000_000)
    )


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
