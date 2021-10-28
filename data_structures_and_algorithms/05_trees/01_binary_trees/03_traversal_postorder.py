from typing import Callable

from tree_structure import Node, node_representation


def traverse_postorder(
    node: Node,
    callback: Callable[[Node], None]
) -> None:
    if node.left is not None:
        traverse_postorder(node.left, callback)

    if node.right is not None:
        traverse_postorder(node.right, callback)

    callback(node)


if __name__ == '__main__':

    root = Node(
        value=1,
        left=Node(
            value=11,
            left=Node(
                value=111,
                left=Node(
                    value=1111,
                    left=None,
                    right=None,
                ),
                right=None,
            ),
            right=Node(
                value=222,
                left=None,
                right=Node(
                    value=2222,
                    left=None,
                    right=None,
                ),
            ),
        ),
        right=Node(
            value=22,
            left=Node(
                value=333,
                left=None,
                right=None,
            ),
            right=Node(
                value=444,
                left=None,
                right=None,
            ),
        )
    )

    print("Original tree")
    print(node_representation(root))

    print("Post-order traversal")
    traverse_postorder(root, lambda x: print(x.value, end=" "))
    print()
