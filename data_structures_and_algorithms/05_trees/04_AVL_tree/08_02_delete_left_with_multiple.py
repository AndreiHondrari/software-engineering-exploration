import functools

from typing import Optional, cast

import matplotlib.pyplot as plt

from tree_structure import (
    node_representation, draw_tree,
)

from avl import (
    Node,
    add_left_child as alc,
    add_right_child as arc,
    validate_tree,
    insert, remove, delete
)


hprint = functools.partial(print, "\n#")


def main() -> None:
    hprint("Deletion")

    values_to_insert = [
        100, 50, 200, 25, 75, 150, 250, 300, 20, 30, 70, 80, 79
    ]
    TARGET = 50

    hprint("Insert values")
    root: Optional[Node] = None
    for x in values_to_insert:
        print(f"Inserting {x} ...")
        root, new_node = insert(root, x)

    hprint("Before")
    print(node_representation(root))
    draw_tree(root)

    hprint("Delete")
    root = delete(cast(Node, root), TARGET)

    hprint("After")
    if root is not None:
        print(node_representation(root))
        draw_tree(root)
    else:
        print("Nothing left")

    plt.show()


if __name__ == "__main__":
    main()
