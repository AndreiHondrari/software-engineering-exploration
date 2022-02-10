
import functools
from typing import Set, Tuple, Optional, Any, Dict

import networkx as nx
from matplotlib import pyplot as plt

from graph import add_edge, add_weight, dijkstra_shortest_path
from graph_utils import draw_graph

hprint = functools.partial(print, "\n#")


def get_layout(g: Any, root: Optional[int] = None) -> Optional[Any]:
    """
    Examples:
    nx.drawing.nx_pydot.pydot_layout(g, prog="dot")
    nx.drawing.layout.planar_layout(g)
    """
    return nx.drawing.nx_pydot.pydot_layout(g, prog="neato", root=root)


def build_graph() -> Tuple[
    Set[int],
    Set[Tuple[int, int]],
    Dict[Tuple[int, int], int]
]:
    vertices: Set[int] = set()
    edges: Set[Tuple[int, int]] = set()
    weights: Dict[Tuple[int, int], int] = dict()

    # insert nodes
    vertices = set([
        5, 20, 100, 50,
        30, 123, 250, 400,
        55, 66, 77, 88, 99, 111,
        1, 2, 3, 4, 5, 6, 7, 8, 9,
    ])

    # insert edges
    proposed_edges = {
        (5, 50): 1,
        (5, 100): 1,
        (20, 50): 1,
        (100, 20): 1,
        (100, 50): 1,
        (30, 123): 1,
        (30, 250): 1,
        (30, 400): 1,
        (123, 250): 1,
        (123, 400): 1,
        (250, 400): 1,
        (55, 66): 1,
        (55, 77): 1,
        (66, 77): 1,
        (88, 99): 1,
        (88, 111): 1,
        (99, 111): 1,
        (55, 88): 1,
        (1, 2): 1,
        (1, 4): 1,
        (2, 3): 1,
        (2, 5): 1,
        (2, 4): 1,
        (3, 5): 1,
        (4, 6): 1,
        (4, 7): 1,
        (5, 7): 1,
        (5, 8): 1,
        (6, 7): 1,
        (6, 9): 1,
        (7, 8): 1,
        (8, 9): 1,
        (100, 30): 1,
        (9, 50): 1,
    }

    for e, w in proposed_edges.items():
        edges = add_edge(edges, e[0], e[1])
        weights = add_weight(weights, e[0], e[1], w)

    return vertices, edges, weights


draw_graph = functools.partial(draw_graph, get_layout=get_layout)

FIG_SCALE = 1.2
MARGIN = 0.05
NODE_SIZE = 400
FONT_SIZE = 8
LAYOUT_ROOT = 1


def main() -> None:
    hprint("Undirected matrix graph")
    V, E, W = build_graph()
    START = 250
    TARGET = START

    M = set([START, TARGET])  # marked
    M_COLOR_MAP = {START: "cyan"}

    fig: plt.Figure = draw_graph(
        V, E, M,
        weights=W,
        subplot=121,
        title="Start and target",
        marked_color_map=M_COLOR_MAP,
        layout_root=LAYOUT_ROOT,
        font_size=FONT_SIZE,
        node_size=NODE_SIZE,
        xmargin=MARGIN,
        ymargin=MARGIN,
    )

    fig.set_size_inches(10 * FIG_SCALE, 6 * FIG_SCALE)

    print(f"Perform Dijkstra shortest path for {START} -> {TARGET}")
    target_found, result_edges = dijkstra_shortest_path(V, E, W, START, TARGET)
    print("target found?:", target_found)
    print("path to target:", result_edges)

    edge_color_map: Dict[Tuple[int, int], str] = {
        e: "red" for e in result_edges
    }
    edge_width_map: Dict[Tuple[int, int], float] = {
        e: 3.0 for e in result_edges
    }
    draw_graph(
        V, E, M, figure=fig,
        weights=W,
        subplot=122, title="Discovered target",
        edge_color_map=edge_color_map,
        edge_width_map=edge_width_map,
        marked_color_map=M_COLOR_MAP,
        layout_root=LAYOUT_ROOT,
        font_size=FONT_SIZE,
        node_size=NODE_SIZE,
        xmargin=MARGIN,
        ymargin=MARGIN,
    )


if __name__ == "__main__":
    main()
    plt.show()
