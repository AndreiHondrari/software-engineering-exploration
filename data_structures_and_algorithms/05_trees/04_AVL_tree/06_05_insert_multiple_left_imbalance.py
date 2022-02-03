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
    validate_tree,
    insert,
)


hprint = functools.partial(print, "\n#")


def main() -> None:
    hprint("Insertion")

    values_to_insert = [100, 50, 200, 150, 250, 25, 75, 20, 30, 70, 80]
    DESTABILIZING_VALUE = 90

    hprint("Insert values")
    root: Optional[Node] = None
    for x in values_to_insert:
        print(f"Inserting {x} ...")
        root = insert(root, x)

    hprint("Before")
    print(node_representation(root))
    draw_tree(root)

    hprint("Imbalance tree")
    root = insert(root, DESTABILIZING_VALUE)

    hprint("After")
    print(node_representation(root))
    draw_tree(root)

    plt.show()


if __name__ == "__main__":
    main()
