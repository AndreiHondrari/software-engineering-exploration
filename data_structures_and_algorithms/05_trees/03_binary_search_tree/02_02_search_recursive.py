from typing import cast, Optional
import matplotlib.pyplot as plt

from bst import BinarySearchTree
from tree_structure import Node, node_representation, draw_tree


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


def _search(node: Node, reference: int) -> Optional[Node]:
    if node.value == reference:
        return node

    if node.left is not None and reference < node.value:
        return _search(node.left, reference)

    if node.right is not None and reference > node.value:
        return _search(node.right, reference)

    return None


def search(bst: BinarySearchTree, reference: int) -> Optional[Node]:
    if bst.root is None:
        return None

    return _search(bst.root, reference)


if __name__ == '__main__':
    bst = BinarySearchTree()

    insert(bst, 50)
    insert(bst, 25)
    insert(bst, 75)
    insert(bst, 20)
    insert(bst, 30)
    insert(bst, 100)
    draw_tree(bst.root)

    print(node_representation(cast(Node, bst.root)))

    x: Optional[Node] = search(bst, 30)

    print(f"Found: {x} \n")

    plt.show()
