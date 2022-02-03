import functools

from typing import Optional

import matplotlib.pyplot as plt

from tree_structure import (
    node_representation, draw_tree,
)

from avl import (
    Node,
    add_left_child as alc,
    add_right_child as arc,
    balance,
)


hprint = functools.partial(print, "\n#")


def build_tree() -> Node:

    root = Node(value="0")

    subroot = arc(root, "A")

    left_subtree = alc(subroot, "B")
    K = alc(left_subtree, "K")
    alc(K, "P")
    arc(K, "Q")
    K.left_height = 1
    K.right_height = 1

    M = arc(left_subtree, "M")
    alc(M, "S")
    T = arc(M, "T")
    arc(T, "Z")
    T.right_height = 1

    M.left_height = 1
    M.right_height = 2

    left_subtree.left_height = 2
    left_subtree.right_height = 3

    right_subtree = arc(subroot, "C")
    alc(right_subtree, "X")
    arc(right_subtree, "Y")

    right_subtree.left_height = 1
    right_subtree.right_height = 1

    subroot.left_height = 4
    subroot.right_height = 2

    root.right_height = 5

    return root


def main() -> None:
    hprint("Balance")

    hprint("Build tree")
    root = build_tree()

    node_representation(root)
    draw_tree(root)

    hprint("Balance right subtree")
    balance(root.right)

    node_representation(root)
    draw_tree(root)

    plt.show()


if __name__ == "__main__":
    main()
