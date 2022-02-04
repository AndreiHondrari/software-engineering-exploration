import functools

from typing import Tuple

import matplotlib.pyplot as plt

from tree_structure import (
    Node,
    node_representation, draw_tree,
    add_left_child as alc,
)

from binary_tree_functions import swap_parent_child

hprint = functools.partial(print, "\n#")


def build_tree() -> Tuple[Node, Node]:
    """
    :return: root, target for swap
    """
    root = Node(value="A")
    B = alc(root, value="B")
    return root, B


def main() -> None:
    hprint("Swapping")
    root, target = build_tree()

    hprint("Before")
    print(node_representation(root))
    draw_tree(root)

    hprint("Swap")
    root = swap_parent_child(root, target)

    hprint("After")
    print(node_representation(root))
    draw_tree(root)

    plt.show()


if __name__ == "__main__":
    main()
