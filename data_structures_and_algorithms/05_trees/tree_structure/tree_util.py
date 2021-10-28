from typing import Optional, Dict, Tuple

import networkx as nx
import matplotlib.pyplot as plt

from .node import Node


def add_left_child(node: Node, value: int) -> Node:
    assert node.left is None
    new_node = Node(value=value, parent=node)
    node.left = new_node
    return new_node


def add_right_child(node: Node, value: int) -> Node:
    assert node.right is None
    new_node = Node(value=value, parent=node)
    node.right = new_node
    return new_node


def node_representation(
    node: 'Node',
    prepend: str = "",
    orientation: str = ""
) -> str:
    node_repr: str = f"{prepend}{orientation} [{node.value}]: {node.control_id}\n"

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
    side: int = 0,
) -> None:
    if node is None:
        return

    g.add_node(node.control_id)
    if node.parent is not None:
        g.add_edge(node.parent.control_id, node.control_id)

    nx.set_node_attributes(g, {
        node.control_id: {
            'data': node.value,
            'side': side
        }
    })

    # fake nodes for empty
    if node.left is None:
        fake_left = Node(value="", parent=node)
        g.add_node(fake_left.control_id)
        g.add_edge(node.control_id, fake_left.control_id)
    if node.right is None:
        fake_right = Node(value="", parent=node)
        g.add_node(fake_right.control_id)
        g.add_edge(node.control_id, fake_right.control_id)

    _construct_nx_tree(g, node.left, 1)
    _construct_nx_tree(g, node.right, 2)


def _compute_positions(g) -> Dict[int, Tuple[int, int]]:
    result = {}

    return result


def draw_tree(
    root: Node,
    fig_scale: int = 1,
    fig_scale_exponent: float = 1.2
) -> None:
    g = nx.DiGraph()
    _construct_nx_tree(g, root)

    positions = _compute_positions(g)

    # prepare graph drawing
    fig = plt.figure(frameon=False)
    INCH_FACTOR = 5  # inches
    fig_scale = int(fig_scale ** fig_scale_exponent)
    fig.set_size_inches(fig_scale * INCH_FACTOR, fig_scale * INCH_FACTOR)

    labels = nx.get_node_attributes(g, 'data')

    nodes_sides = nx.get_node_attributes(g, 'side')
    color_map = []
    for n in g:
        node_side: int = nodes_sides.get(n, 99)
        if node_side == 0:
            color_map.append("red")
        elif node_side == 1:
            color_map.append("green")
        elif node_side == 2:
            color_map.append("blue")
        else:
            color_map.append("#e3e3e3")

    # actually draw the graph and save it to a PNG.
    nx.draw_networkx(
        g,
        with_labels=True,
        labels=labels,
        node_size=fig_scale**2 * 600,
        # node_color='#e5e5e5',
        node_color=color_map,
        font_weight='bold', font_size=str(10 * fig_scale),
        pos=nx.drawing.nx_pydot.pydot_layout(g, prog='dot')
    )
