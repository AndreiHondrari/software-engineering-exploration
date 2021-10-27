from typing import cast, Optional

from bst import BinarySearchTree, Node, node_representation


def _insert(node: Node, new_value: int) -> Optional[Node]:
    if new_value == node.value:
        return None

    if new_value < node.value:
        if node.left is None:
            new_node = Node(value=new_value, parent=node)
            node.left = new_node
            return new_node
        else:
            return _insert(node.left, new_value)

    else:
        if node.right is None:
            new_node = Node(value=new_value, parent=node)
            node.right = new_node
            return new_node
        else:
            return _insert(node.right, new_value)


def insert(bst: BinarySearchTree, new_value: int) -> Optional[Node]:
    if bst.root is None:
        new_root = Node(value=new_value)
        bst.root = new_root
        return new_root

    return _insert(bst.root, new_value)


def remove_from_tree(target: Node) -> None:
    parent: Optional[Node] = target.parent
    left_exists: bool = target.left is not None
    right_exists: bool = target.right is not None

    replacement: Optional[Node] = None

    # determine replacement
    if left_exists and not right_exists:
        replacement = target.left

    if not left_exists and right_exists:
        replacement = target.right

    if left_exists and right_exists:
        p: Optional[Node] = target.right
        while p is not None and p.left is not None:
            p = p.left

        remove_from_tree(cast(Node, p))
        replacement = p
        cast(Node, replacement).left = target.left
        cast(Node, replacement).right = target.right

    # handle parenting
    if parent is not None:
        if replacement is not None:
            replacement.parent = parent

        if parent.left is target:
            parent.left = replacement

        if parent.right is target:
            parent.right = replacement


if __name__ == '__main__':
    bst = BinarySearchTree()

    insert(bst, 50)
    target_node = insert(bst, 25)
    insert(bst, 75)
    insert(bst, 20)
    insert(bst, 19)
    insert(bst, 21)
    insert(bst, 30)
    insert(bst, 26)
    insert(bst, 27)
    insert(bst, 31)
    insert(bst, 100)

    print("BEFORE")
    print(node_representation(cast(Node, bst.root)))

    print(f"Remove {target_node} \n")
    remove_from_tree(cast(Node, target_node))

    print("AFTER")
    print(node_representation(cast(Node, bst.root)))
