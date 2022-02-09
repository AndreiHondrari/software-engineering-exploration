
from typing import (
    Set, Tuple, Optional, Callable, Any, Dict, cast,
)

import networkx as nx
import matplotlib.pyplot as plt


def draw_graph(
    vertices: Set[int],
    edges: Set[Tuple[int, int]],
    marked_nodes: Set[int] = set(),
    get_layout: Optional[Callable[[Any], Any]] = None,
    figure: Optional[plt.Figure] = None,
    subplot: Optional[int] = None,
    title: Optional[str] = None,
    color_map: Dict[int, str] = {},
    edge_color_map: Dict[Tuple[int, int], str] = {},
    edge_width_map: Dict[Tuple[int, int], float] = {},
    marked_color_map: Dict[Tuple[int, int], str] = {},
    layout_root: Optional[int] = None,
    node_size: int = 600,
    font_size=10,
    xmargin: float = 0.2,
    ymargin: float = 0.2,
) -> plt.Figure:

    active_figure = figure

    g = nx.Graph()

    # add nodes and edges
    for vertex in vertices:
        g.add_node(vertex)

    for edge in edges:
        g.add_edge(edge[0], edge[1])

    # compute values for nodes and edges
    node_colors = []
    for n in g:
        if n in color_map:
            node_colors.append(color_map[n])
        else:
            if n in marked_nodes:
                if n in marked_color_map:
                    node_colors.append(marked_color_map[n])
                else:
                    node_colors.append("#f00")
            else:
                node_colors.append("#0f0")

    edge_colors = []
    edge_widths = []
    for e in g.edges:

        e_reversed = cast(Tuple[int, int], tuple(reversed(e)))
        if e in edge_color_map:
            edge_colors.append(edge_color_map[e])
        elif e_reversed in edge_color_map:
            edge_colors.append(edge_color_map[e_reversed])
        else:
            edge_colors.append("black")

        if e in edge_width_map:
            edge_widths.append(edge_width_map[e])
        elif e_reversed in edge_width_map:
            edge_widths.append(edge_width_map[e_reversed])
        else:
            edge_widths.append(1.0)

    # draw to screen
    if active_figure is None:
        active_figure = plt.figure(frameon=True)

    if get_layout is None:
        pos = None
    else:
        pos = get_layout(g, root=layout_root)

    axes: Optional[plt.Axes] = None
    if subplot is not None:
        axes = plt.subplot(subplot)

    # draw nodes
    nx.draw_networkx_nodes(
        g,
        pos=pos,
        node_color=node_colors,
        node_size=node_size,
    )

    # draw edges
    nx.draw_networkx_edges(
        g,
        pos=pos,
        edge_color=edge_colors,
        width=edge_widths,
    )

    # draw labels
    nx.draw_networkx_labels(
        g,
        pos=pos,
        font_weight="bold",
        font_size=font_size
    )

    if axes is None:
        axes = active_figure.axes[0]

    axes.set_xmargin(xmargin)
    axes.set_ymargin(ymargin)

    if title is not None:
        axes.set_title(title)

    return active_figure
