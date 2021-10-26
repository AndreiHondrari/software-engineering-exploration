from typing import Callable, Deque

from collections import deque

from binary_tree import Node, node_representation


def traverse_levelorder(
    node: Node,
    callback: Callable[[Node], None]
) -> None:
    queue_candidates: Deque[Node] = deque([node])

    while len(queue_candidates) > 0:
        p: Node = queue_candidates.popleft()

        callback(p)

        if p.left is not None:
            queue_candidates.append(p.left)

        if p.right is not None:
            queue_candidates.append(p.right)


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

    print("Level-order traversal")
    traverse_levelorder(root, lambda x: print(x.value, end=" "))
    print()
