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


def main() -> None:
    hprint("Left rotation")
    root = Node(value="A")
    n1 = add_right_child(root, "B")
    add_right_child(n1, "C")

    hprint("Before")
    print(node_representation(root))
    draw_tree(root)

    root = rotate_left(root)

    hprint("After")
    print(node_representation(root))
    draw_tree(root)

    plt.show()


if __name__ == "__main__":
    main()
