import matplotlib.pyplot as plt

from tree_structure import Node, node_representation, draw_tree
from binary_tree_functions import rotate_right

if __name__ == '__main__':
    root = Node(value=1)

    print("Original tree")
    print(node_representation(root))
    draw_tree(root)

    print("Rotate right")
    root = rotate_right(root)
    print(node_representation(root))
    draw_tree(root)

    print()
    plt.show()
