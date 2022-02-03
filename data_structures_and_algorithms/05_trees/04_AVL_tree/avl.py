import functools

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


def _insert(node: Node, value: Any) -> Tuple[bool, Node, Optional[Node]]:
    """
    :return: insertion status, subroot, new node
    """
    if value == node.value:
        return False, node, None

    inserted = False
    new_node: Optional[Node] = None

    # handle smaller value
    if value < node.value:
        if node.left is None:
            new_node = Node(parent=node, value=value)
            node.left = new_node
            node.left_height = 1
            inserted = True
        else:
            inserted, new_left, new_node = _insert(node.left, value)
            node.left_height = new_left.height

    # handle bigger value
    if value > node.value:
        if node.right is None:
            new_node = Node(parent=node, value=value)
            node.right = new_node
            node.right_height = 1
            inserted = True
        else:
            inserted, new_right, new_node = _insert(node.right, value)
            node.right_height = new_right.height

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

        return True, new_subroot, new_node

    return False, node, None


def insert(root: Optional[Node], value: Any) -> Tuple[Node, Node]:
    # just create the root if it doesn't exist
    if root is None:
        new_node = Node(value=value)
        return new_node, new_node

    _, root, new_node = _insert(root, value)

    return root, new_node


def get_leftmost(node: Node) -> Node:
    if node.left is None:
        return node

    return get_leftmost(node.left)


def get_rightmost(node: Node) -> Node:
    if node.right is None:
        return node

    return get_rightmost(node.right)


def remove(node: Node) -> Tuple[Optional[Node], Node]:
    successor: Optional[Node] = None

    left = node.left
    right = node.right
    balance_factor = node.balance_factor

    deleted_node = node
    deleted_node.left = None
    deleted_node.left_height = 0
    deleted_node.right = None
    deleted_node.right_height = 0
    deleted_node.parent = None

    # handle remove with both children
    if right is not None and left is not None:

        # from left
        if balance_factor >= 0:
            successor = cast(Node, left)

            # obtain rightmost of left
            rightmost = get_rightmost(left)
            new_left = None

            if rightmost is not left:
                rightmost_parent = rightmost.parent

                # remove the rightmost from its location
                new_rightmost, new_left = remove(rightmost)

                # rewire rightmost parent
                rightmost_parent.right = new_rightmost
                if new_rightmost is not None:
                    new_rightmost.parent = rightmost_parent

                # rewire removed rightmost
                new_left.parent = successor
                new_left.left = successor.left
                if new_left.left is not None:
                    new_left.left.parent = new_left

                new_left.right = successor.right
                if new_left.right is not None:
                    new_left.right.parent = new_left

                # update heights
                if new_left.left is None:
                    new_left.left_height = 0
                else:
                    new_left.left_height = new_left.left.height

                if new_left.right is None:
                    new_left.right_height = 0
                else:
                    new_left.right_height = new_left.right.height

            # rewire successor
            if new_left is not None:
                successor.left = new_left
                new_left.parent = successor

            successor.right = right
            right.parent = successor

        # from right
        else:
            successor = cast(Node, right)

            # obtain leftmost of right
            leftmost = get_leftmost(right)
            new_right = None

            if leftmost is not right:
                leftmost_parent = leftmost.parent

                # remove the leftmost from its location
                new_leftmost, new_right = remove(leftmost)

                # rewire leftmost parent
                leftmost_parent.left = new_leftmost
                if new_leftmost is not None:
                    new_leftmost.parent = leftmost_parent

                # rewire removed leftmost
                new_right.parent = successor
                new_right.left = successor.left
                if new_right.left is not None:
                    new_right.left.parent = new_right

                new_right.right = successor.right
                if new_right.right is not None:
                    new_right.right.parent = new_right

                # update heights
                if new_right.left is None:
                    new_right.left_height = 0
                else:
                    new_right.left_height = new_right.left.height

                if new_right.right is None:
                    new_right.right_height = 0
                else:
                    new_right.right_height = new_right.right.height

            # rewire successor
            successor.left = left
            left.parent = successor

            if new_right is not None:
                successor.right = new_right
                new_right.parent = successor

    # handle remove with single child
    else:
        if left is not None:
            successor = left

        if right is not None:
            successor = right

    # reset successor parent
    if successor is not None:
        successor.parent = None

        sleft = successor.left
        successor.left_height = 0 if sleft is None else sleft.height

        sright = successor.right
        successor.right_height = 0 if sright is None else sright.height

    return successor, deleted_node


def delete(node: Node, value: Any) -> Optional[Node]:
    successor: Optional[Node] = node

    # handle match
    if node.value == value:
        parent = node.parent
        is_left: Optional[bool] = (
            None if parent is None else parent.left is node
        )
        successor, removed_node = remove(node)

        if successor is not None:
            successor.parent = parent

        successor_height = 0 if successor is None else successor.height

        if parent is not None:
            if is_left:
                parent.left = successor
                parent.left_height = successor_height
            else:
                parent.right = successor
                parent.right_height = successor_height

    # handle lesser
    elif value < node.value:
        if node.left is not None:
            node.left = delete(node.left, value)
            if node.left is not None:
                node.left_height = node.left.height

    # handle greater
    elif value > node.value:
        if node.right is not None:
            node.right = delete(node.right, value)
            if node.right is not None:
                node.right_height = node.right.height

    # re-balance
    if successor is not None:
        successor = balance(successor)

    return successor
