import functools

import matplotlib.pyplot as plt

from tree_structure import (
    add_left_child, add_right_child,
    node_representation, draw_tree,
)

from avl import (
    Node,
    rotate_left, rotate_right,
    rotate_left_right, rotate_right_left,
)


hprint = functools.partial(print, "\n#")


def build_tree() -> Node:
    root = Node(value="A")

    left_subtree = add_left_child(root, "B")
    add_left_child(left_subtree, "X")
    add_right_child(left_subtree, "Y")

    right_subtree = add_right_child(root, "C")
    K = add_left_child(right_subtree, "K")
    add_left_child(K, "P")
    add_right_child(K, "Q")

    M = add_right_child(right_subtree, "M")
    add_left_child(M, "S")
    add_right_child(M, "T")

    return root


def main() -> None:
    hprint("Left rotation")
    root = build_tree()

    hprint("Before")
    print(node_representation(root))
    draw_tree(root)

    hprint("1 rot")
    root = rotate_left(root)
    print(node_representation(root))
    draw_tree(root)

    hprint("2 rot")
    root = rotate_left(root)
    print(node_representation(root))
    draw_tree(root)

    hprint("3 rot")
    root = rotate_left(root)
    print(node_representation(root))
    draw_tree(root)

    hprint("4 rot")
    root = rotate_left(root)
    print(node_representation(root))
    draw_tree(root)

    plt.show()


if __name__ == "__main__":
    main()
