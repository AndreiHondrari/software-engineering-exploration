
import functools
from typing import Set, Tuple, Optional, Any, Dict

import networkx as nx
from matplotlib import pyplot as plt

from graph import add_edge, breadth_first_search
from graph_utils import draw_graph

hprint = functools.partial(print, "\n#")


def get_layout(g: Any, root: Optional[int] = None) -> Optional[Any]:
    """
    Examples:
    nx.drawing.nx_pydot.pydot_layout(g, prog="dot")
    nx.drawing.layout.planar_layout(g)
    """
    return nx.drawing.nx_pydot.pydot_layout(g, prog="neato", root=root)


def build_graph() -> Tuple[Set[int], Set[Tuple[int, int]]]:
    vertices: Set[int] = set()
    edges: Set[Tuple[int, int]] = set()

    SIZE = 11
    assert SIZE % 2 != 0

    # generate mesh matrix
    matrix: Dict[Tuple[int, int], int] = {}

    count = 1
    for i in range(SIZE):
        for j in range(SIZE):
            matrix[i, j] = count
            count += 1

    # generate vertices and edges
    for i in range(SIZE):
        for j in range(SIZE):
            node = matrix[i, j]
            vertices.add(node)

            up = None if (i - 1) < 0 else matrix[i - 1, j]
            down = None if (i + 1) >= SIZE else matrix[i + 1, j]
            left = None if (j - 1) < 0 else matrix[i, j - 1]
            right = None if (j + 1) >= SIZE else matrix[i, j + 1]

            if up is not None:
                edges = add_edge(edges, node, up)

            if down is not None:
                edges = add_edge(edges, node, down)

            if left is not None:
                edges = add_edge(edges, node, left)

            if right is not None:
                edges = add_edge(edges, node, right)

    return vertices, edges


draw_graph = functools.partial(draw_graph, get_layout=get_layout)

FIG_SCALE = 1.4
LAYOUT_ROOT = 1
MARGIN = 0.01
NODE_SIZE = 300
FONT_SIZE = 8


def main() -> None:
    hprint("Undirected matrix graph")
    V, E = build_graph()
    START = 61
    TARGET = 29

    M = set([START, TARGET])  # marked
    M_COLOR_MAP = {START: "cyan"}

    fig: plt.Figure = draw_graph(
        V, E, M,
        subplot=121,
        title="Start and target",
        marked_color_map=M_COLOR_MAP,
        layout_root=LAYOUT_ROOT,
        node_size=NODE_SIZE,
        font_size=FONT_SIZE,
        xmargin=MARGIN,
        ymargin=MARGIN,
    )

    fig.set_size_inches(10 * FIG_SCALE, 6 * FIG_SCALE)

    print(f"Perform breadth first search for {TARGET} from {START}")
    target_found, result_edges = breadth_first_search(V, E, START, TARGET)
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
        subplot=122, title="Discovered target",
        edge_color_map=edge_color_map,
        edge_width_map=edge_width_map,
        marked_color_map=M_COLOR_MAP,
        layout_root=LAYOUT_ROOT,
        node_size=NODE_SIZE,
        font_size=FONT_SIZE,
        xmargin=MARGIN,
        ymargin=MARGIN,
    )


if __name__ == "__main__":
    main()
    plt.show()
