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


if __name__ == '__main__':
    bst = BinarySearchTree()

    insert(bst, 100)
    insert(bst, 50)
    insert(bst, 150)
    insert(bst, 25)
    insert(bst, 75)
    insert(bst, 125)
    insert(bst, 175)
    insert(bst, 10)
    insert(bst, 30)
    insert(bst, 60)
    insert(bst, 80)
    insert(bst, 110)
    insert(bst, 130)
    insert(bst, 160)
    insert(bst, 180)
    insert(bst, 5)
    insert(bst, 15)
    insert(bst, 27)
    insert(bst, 35)
    insert(bst, 55)
    insert(bst, 65)
    insert(bst, 77)
    insert(bst, 95)
    insert(bst, 105)
    insert(bst, 115)
    insert(bst, 127)
    insert(bst, 140)
    insert(bst, 155)
    insert(bst, 165)
    insert(bst, 180)
    insert(bst, 177)
    insert(bst, 190)

    print(node_representation(cast(Node, bst.root)))
    draw_tree(bst.root, fig_scale=1)

    plt.show()
