import dataclasses as dc
from typing import Optional, Any, Dict

import networkx as nx
import matplotlib.pyplot as plt

NODE_REPR: str = "Node({value})"


@dc.dataclass
class Node:
    value: Any
    parent: Optional['Node'] = dc.field(default=None, repr=False)
    left: Optional['Node'] = dc.field(default=None, repr=False)
    right: Optional['Node'] = dc.field(default=None, repr=False)


@dc.dataclass
class BinarySearchTree:
    root: Optional[Node] = None


def node_representation(
    node: 'Node',
    prepend: str = "",
    orientation: str = ""
) -> str:
    node_repr: str = f"{prepend}{orientation} [{node.value}]: {id(node)}\n"

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
    node: Optional[Node]
) -> None:
    if node is None:
        return

    g.add_node(id(node))
    if node.parent is not None:
        g.add_edge(id(node.parent), id(node))

    nx.set_node_attributes(g, {
        id(node): {
            'data': node.value,
        }
    })
    _construct_nx_tree(g, node.left)
    _construct_nx_tree(g, node.right)


def draw_tree(
    root: Node,
    fig_scale: int = 1,
    fig_scale_exponent: float = 1.2
) -> None:
    g = nx.DiGraph()
    _construct_nx_tree(g, root)

    # prepare graph drawing
    fig = plt.figure(frameon=False)
    INCH_FACTOR = 5  # inches
    fig_scale = int(fig_scale ** fig_scale_exponent)
    fig.set_size_inches(fig_scale * INCH_FACTOR, fig_scale * INCH_FACTOR)

    labels = nx.get_node_attributes(g, 'data')

    # actually draw the graph and save it to a PNG.
    nx.draw_networkx(
        g,
        with_labels=True,
        labels=labels,
        node_size=fig_scale**2 * 600,
        node_color='#e5e5e5',
        font_weight='bold', font_size=str(10 * fig_scale),
        pos=nx.drawing.nx_pydot.pydot_layout(g, prog='dot')
    )
