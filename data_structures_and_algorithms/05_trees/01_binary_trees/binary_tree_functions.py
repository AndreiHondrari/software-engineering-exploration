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
