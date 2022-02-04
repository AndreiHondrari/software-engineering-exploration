import functools

from typing import Tuple

import matplotlib.pyplot as plt

from tree_structure import (
    Node,
    node_representation, draw_tree, validate_tree,
    add_left_child as alc,
    add_right_child as arc,
)

from binary_tree_functions import swap_parent_child

hprint = functools.partial(print, "\n#")


def build_tree() -> Tuple[Node, Node, Node]:
    """
    :return: root, target parent, target child
    """
    root = Node(value="A")

    B = alc(root, value="B")

    M = alc(B, "M")
    alc(M, "R")
    arc(M, "S")

    N = arc(B, "N")
    alc(N, "T")
    arc(N, "U")

    C = arc(root, value="C")
    alc(C, "P")
    arc(C, "Q")

    return root, B, M


def main() -> None:
    hprint("Swapping")
    root, target_parent, target_child = build_tree()

    hprint("Before")
    print(node_representation(root))
    draw_tree(root)

    hprint("Swap")
    swap_parent_child(target_parent, target_child)

    hprint("After")
    errors = validate_tree(None, root)
    if len(errors) == 0:
        print(node_representation(root))
        draw_tree(root)
    else:
        print("ERRORS:", errors)

    plt.show()


if __name__ == "__main__":
    main()
