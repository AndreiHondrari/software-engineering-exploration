
import functools
from typing import Set, Tuple, Optional, Any

import networkx as nx
from matplotlib import pyplot as plt

from graph import add_edge, delete
from graph_utils import draw_graph

hprint = functools.partial(print, "\n#")


def get_layout(g: Any) -> Optional[Any]:
    """
    Examples:
    nx.drawing.nx_pydot.pydot_layout(g, prog="dot")
    nx.drawing.layout.planar_layout(g)
    """
    return nx.drawing.nx_pydot.pydot_layout(g, prog="twopi")


def build_graph() -> Tuple[Set[int], Set[Tuple[int, int]]]:
    vertices: Set[int] = set()
    edges: Set[Tuple[int, int]] = set()

    # insert nodes
    vertices.add(5)
    vertices.add(20)
    vertices.add(100)
    vertices.add(50)

    vertices.add(30)
    vertices.add(123)
    vertices.add(250)
    vertices.add(400)

    # insert
    edges = add_edge(edges, 5, 50)
    edges = add_edge(edges, 5, 100)
    edges = add_edge(edges, 20, 50)
    edges = add_edge(edges, 100, 20)
    edges = add_edge(edges, 100, 50)

    edges = add_edge(edges, 30, 123)
    edges = add_edge(edges, 30, 250)
    edges = add_edge(edges, 30, 400)
    edges = add_edge(edges, 123, 250)
    edges = add_edge(edges, 123, 400)
    edges = add_edge(edges, 250, 400)

    edges = add_edge(edges, 100, 30)

    return vertices, edges


draw_graph = functools.partial(draw_graph, get_layout=get_layout)

FIG_SCALE = 1.2


def main() -> None:
    hprint("Undirected matrix graph")
    V, E = build_graph()
    TARGET_FOR_DELETE = 400

    M = set([TARGET_FOR_DELETE])  # marked

    fig: plt.Figure = draw_graph(V, E, M, subplot=121, title="Before")
    fig.set_size_inches(8 * FIG_SCALE, 6 * FIG_SCALE)

    print("Deleting node ...")
    V, E = delete(V, E, TARGET_FOR_DELETE)

    draw_graph(V, E, figure=fig, subplot=122, title="After")


if __name__ == "__main__":
    main()
    plt.show()
