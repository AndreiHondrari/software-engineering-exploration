import functools

from typing import Optional, cast

import matplotlib.pyplot as plt

from tree_structure import (
    node_representation, draw_tree, validate_tree,
)

from avl import (
    Node,
    add_left_child as alc,
    add_right_child as arc,
    insert, remove, delete
)


hprint = functools.partial(print, "\n#")


def main() -> None:
    hprint("Removal")

    values_to_insert = [100]

    hprint("Insert values")
    root: Optional[Node] = None
    for x in values_to_insert:
        print(f"Inserting {x} ...")
        root, new_node = insert(root, x)

    hprint("Before")
    print(node_representation(root))
    draw_tree(root)

    hprint("Remove")
    root, removed_node = remove(cast(Node, root))

    hprint("After")
    print(root)

    plt.show()


if __name__ == "__main__":
    main()
