import matplotlib.pyplot as plt

from tree_structure import (
    Node,
    add_left_child, add_right_child,
    node_representation, draw_tree
)
from binary_tree_functions import rotate_right

if __name__ == '__main__':
    root = Node(value=0)
    root_left = add_left_child(root, 11)
    add_left_child(root_left, 22)
    add_right_child(root_left, 33)
    root_right = add_right_child(root, 44)
    add_left_child(root_right, 55)
    add_right_child(root_right, 66)

    print("Original tree")
    print(node_representation(root))
    draw_tree(root)

    print("Rotate right")
    root = rotate_right(root)

    print(node_representation(root))
    draw_tree(root)

    print()
    plt.show()
