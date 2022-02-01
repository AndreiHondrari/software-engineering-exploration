# type: ignore

import matplotlib.pyplot as plt

from tree_structure import (
    Node,
    add_right_child,
    node_representation, draw_tree
)
from binary_tree_functions import rotate_left


if __name__ == '__main__':
    root = Node(value=1)
    n1 = add_right_child(root, 11)
    add_right_child(n1, 22)

    print("Original tree")
    print(node_representation(root))
    draw_tree(root)

    print("Rotate right")
    root = rotate_left(root)
    print(node_representation(root))
    draw_tree(root)

    print()
    plt.show()
