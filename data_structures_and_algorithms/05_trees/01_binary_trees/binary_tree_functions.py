from tree_structure import Node


def rotate_right(root: Node) -> Node:
    new_root = root.left

    # can't rotate anymore
    if new_root is None:
        return root

    # obtain candidate
    root.left = None
    new_root.parent = None

    # get rightmost for new root placement
    right_most = new_root

    while right_most.right is not None:
        right_most = right_most.right

    right_most.right = root
    root.parent = right_most

    return new_root


def rotate_left(root: Node) -> Node:
    new_root = root.right

    if new_root is None:
        return root

    root.right = None
    new_root.parent = None

    left_most = new_root

    while left_most.left is not None:
        left_most = left_most.left

    left_most.left = root
    root.parent = left_most

    return new_root
