import functools

from typing import Optional

import matplotlib.pyplot as plt

from tree_structure import (
    node_representation, draw_tree, validate_tree,
)

from avl import (
    Node,
    add_left_child as alc,
    add_right_child as arc,
    insert,
)


hprint = functools.partial(print, "\n#")


def main() -> None:
    hprint("Insertion")

    values_to_insert = [30, 10, 20]

    hprint("Insert values")
    root: Optional[Node] = None
    for x in values_to_insert:
        print(f"Inserting {x} ...")
        root, new_node = insert(root, x)

        errors = validate_tree(None, root)

        if len(errors) == 0:
            print(node_representation(root))
            draw_tree(root)
        else:
            print("ERRORS:", errors)

    plt.show()


if __name__ == "__main__":
    main()
