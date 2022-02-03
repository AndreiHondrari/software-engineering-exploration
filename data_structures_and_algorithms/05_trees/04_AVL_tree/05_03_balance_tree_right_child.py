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
    root = Node(value="A")
    arc(root, "B")
    root.right_height = 1
    return root


def main() -> None:
    hprint("Balance")

    hprint("Build tree")
    root = build_tree()

    node_representation(root)
    draw_tree(root)

    hprint("Balance tree")
    root = balance(root)

    node_representation(root)
    draw_tree(root)

    plt.show()


if __name__ == "__main__":
    main()
