import enum
import dataclasses as dc
from typing import (
    Optional, Dict, Tuple, List, DefaultDict, Type, TypeVar, Any, Callable
)
from collections import defaultdict

import networkx as nx
import matplotlib.pyplot as plt

from .node import Node

T = TypeVar('T')


@enum.unique
class NodeSide(enum.IntEnum):
    ROOT = enum.auto()
    LEFT = enum.auto()
    RIGHT = enum.auto()


@dc.dataclass(frozen=True)
class TreeError:
    node: 'Node'
    parent: Optional['Node'] = None
    description: Optional[str] = None


def validate_tree(
    parent_node: Optional[Node],
    node: Node
) -> List[TreeError]:
    errors = []

    # current node validation
    if node.parent != parent_node:
        errors.append(
            TreeError(
                parent=parent_node,
                node=node,
                description=f"Actual parent is {node.parent}"
            )
        )

    # subtree validation
    if node.left is not None:
        errors += validate_tree(node, node.left)

    if node.right is not None:
        errors += validate_tree(node, node.right)

    return errors


def add_left_child(
    node: T,
    value: Any,
    klass: Type[T] = Node
) -> T:
    assert node.left is None
    new_node = klass(value=value, parent=node)
    node.left = new_node
    return new_node


def add_right_child(
    node: T,
    value: Any,
    klass: Type[T] = Node
) -> T:
    assert node.right is None
    new_node = klass(value=value, parent=node)
    node.right = new_node
    return new_node


def node_representation(
    node: 'Node',
    prepend: str = "",
    orientation: str = ""
) -> str:
    node_repr: str = (
        f"{prepend}{orientation} [{node.value}]: {node.control_id}\n"
    )

    prepend = "  " if (prepend == "") else (prepend + "  ")

    if (node.left is not None):
        left_repr: str = node_representation(node.left, prepend, "L")
        node_repr += left_repr

    if (node.right is not None):
        right_repr: str = node_representation(node.right, prepend, "R")
        node_repr += right_repr

    return node_repr


def _construct_nx_tree(
    g: nx.Graph,
    node: Optional[Node],
    side: NodeSide = NodeSide.ROOT,
    level: int = 0
) -> None:
    if node is None:
        return

    g.add_node(node.control_id)
    if node.parent is not None:
        g.add_edge(node.parent.control_id, node.control_id)

    nx.set_node_attributes(g, {
        node.control_id: {
            'data': node.value,
            'side': side,
            'level': level,
            'parent': (
                node.parent.control_id if node.parent is not None else None
            )
        }
    })

    _construct_nx_tree(g, node.left, NodeSide.LEFT, level + 1)
    _construct_nx_tree(g, node.right, NodeSide.RIGHT, level + 1)


def _max_level_for_node(
    node: Node,
    level: int = 0,
    max_level: int = 0
) -> int:

    left_max: int = 0
    right_max: int = 0
    if node.left is not None:
        left_max = _max_level_for_node(node.left, level + 1, max_level)

    if node.right is not None:
        right_max = _max_level_for_node(node.right, level + 1, max_level)

    return max(level, max(left_max, right_max))


def _compute_positions(
    g: nx.DiGraph,
    root: Node,
    max_level: int
) -> Dict[int, Tuple[int, int]]:

    positions: Dict[int, Tuple[int, int]] = {}

    node_sides: Dict[int, NodeSide] = nx.get_node_attributes(g, 'side')
    node_levels: Dict[int, int] = nx.get_node_attributes(g, 'level')
    node_parents: Dict[int, Optional[int]] = (
        nx.get_node_attributes(g, 'parent')
    )

    # group nodes by level
    nodes_by_level: DefaultDict[int, List[int]] = defaultdict(list)
    for n in g:
        nodes_by_level[node_levels[n]].append(n)

    nodes_by_level.default_factory = None

    # process node positions
    for level in nodes_by_level:
        for n in nodes_by_level[level]:
            parent: Optional[int] = node_parents[n]
            node_side: NodeSide = node_sides[n]

            parent_x: int = positions[parent][0] if parent is not None else 0

            y = -level
            if node_side == NodeSide.LEFT:
                x = parent_x - (2**(max_level - level + 1) // 2)
            elif node_side == NodeSide.RIGHT:
                x = parent_x + (2**(max_level - level + 1) // 2)
            else:
                x = 0

            positions[n] = (x, y,)

    return positions


def draw_tree(root: Node, fig_scale: int = 1) -> None:
    g = nx.DiGraph()
    _construct_nx_tree(g, root)

    max_level: int = _max_level_for_node(root)
    positions = _compute_positions(g, root, max_level)
    total_node_count: int = 2**max_level

    # prepare graph drawing
    INCH_FACTOR = 3 * fig_scale
    fig = plt.figure(frameon=False)
    fig.set_size_inches(
        INCH_FACTOR * (total_node_count / (max_level + 1)),
        INCH_FACTOR
    )

    labels = nx.get_node_attributes(g, 'data')

    nodes_sides = nx.get_node_attributes(g, 'side')
    color_map = []
    for n in g:
        node_side: int = nodes_sides.get(n, 99)
        if node_side == NodeSide.ROOT:
            color_map.append("red")
        elif node_side == NodeSide.LEFT:
            color_map.append("lime")
        elif node_side == NodeSide.RIGHT:
            color_map.append("cyan")
        else:
            color_map.append("#e3e3e3")

    # actually draw the graph and save it to a PNG.
    nx.draw_networkx(
        g,
        with_labels=True,
        labels=labels,
        node_size=600 * fig_scale,
        node_color=color_map,
        font_weight='bold',
        font_size=str(10 * fig_scale),
        pos=positions
    )
