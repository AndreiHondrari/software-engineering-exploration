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


if __name__ == '__main__':
    bst = BinarySearchTree()

    insert(bst, 50)
    insert(bst, 25)
    insert(bst, 75)
    insert(bst, 20)
    insert(bst, 30)
    insert(bst, 100)

    print(node_representation(cast(Node, bst.root)))
