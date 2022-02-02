import functools

import matplotlib.pyplot as plt

from tree_structure import (
    node_representation, draw_tree,
)

from avl import (
    Node,
    add_left_child as alc,
    add_right_child as arc,
    rotate_left, rotate_right,
    rotate_left_right, rotate_right_left,
)


hprint = functools.partial(print, "\n#")


def build_tree() -> Node:
    root = Node(value="A")
    B = arc(root, "B")
    arc(B, "C")
    return root


def main() -> None:
    hprint("Right-Left rotation")

    root = build_tree()

    hprint("Before")
    print(node_representation(root))
    draw_tree(root)

    root = rotate_right_left(root)

    hprint("After")
    print(node_representation(root))
    draw_tree(root)

    plt.show()


if __name__ == "__main__":
    main()
