import functools

import matplotlib.pyplot as plt

from tree_structure import (
    add_left_child as alc,
    add_right_child as arc,
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
    left_subtree = alc(root, "B")
    K = alc(left_subtree, "K")
    alc(K, "P")
    arc(K, "Q")

    M = arc(left_subtree, "M")
    alc(M, "S")
    arc(M, "T")

    right_subtree = arc(root, "C")
    alc(right_subtree, "X")
    arc(right_subtree, "Y")

    return root


def main() -> None:
    hprint("Right rotation")
    root = build_tree()

    hprint("Before")
    print(node_representation(root))
    draw_tree(root)

    hprint("1 rot")
    root = rotate_right(root)
    print(node_representation(root))
    draw_tree(root)

    hprint("2 rot")
    root = rotate_right(root)
    print(node_representation(root))
    draw_tree(root)

    hprint("3 rot")
    root = rotate_right(root)
    print(node_representation(root))
    draw_tree(root)

    hprint("4 rot")
    root = rotate_right(root)
    print(node_representation(root))
    draw_tree(root)

    plt.show()


if __name__ == "__main__":
    main()
