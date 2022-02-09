
import functools
from typing import Set, Tuple, Optional, Any

import networkx as nx
from matplotlib import pyplot as plt

from graph import add_edge
from graph_utils import draw_graph

hprint = functools.partial(print, "\n#")


def get_layout(g: Any, root: Optional[int] = None) -> Optional[Any]:
    """
    Examples:
    nx.drawing.nx_pydot.pydot_layout(g, prog="dot")
    nx.drawing.layout.planar_layout(g)
    """
    return nx.drawing.nx_pydot.pydot_layout(g, prog="twopi", root=root)


def main() -> None:
    hprint("Undirected matrix graph")
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
    edges = add_edge(edges, 5, 20)
    edges = add_edge(edges, 5, 100)
    edges = add_edge(edges, 100, 20)
    edges = add_edge(edges, 100, 50)

    edges = add_edge(edges, 30, 123)
    edges = add_edge(edges, 30, 250)
    edges = add_edge(edges, 30, 400)

    # mark some
    marked_nodes = set([100, 30])

    draw_graph(vertices, edges, marked_nodes, get_layout, layout_root=100)


if __name__ == "__main__":
    main()
    plt.show()
