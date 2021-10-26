from typing import Callable

from binary_tree import Node, node_representation


def traverse_inorder(
    node: Node,
    callback: Callable[[Node], None]
) -> None:
    if node.left is not None:
        traverse_inorder(node.left, callback)

    callback(node)

    if node.right is not None:
        traverse_inorder(node.right, callback)


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

    print("In-order traversal")
    traverse_inorder(root, lambda x: print(x.value, end=" "))
    print()
