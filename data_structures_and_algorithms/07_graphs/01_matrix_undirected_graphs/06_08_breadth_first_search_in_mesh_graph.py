
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

    # insert nodes
    vertices = set([
        1,
        11, 22, 33, 44, 55, 66, 77, 88,
        110, 120, 130, 140, 150, 160, 170, 180, 190,
        200, 210, 220, 230, 240, 250,
        300, 310, 320, 330, 340, 350, 360, 370, 380, 390,
        400, 410, 420, 430, 440, 450, 460, 470, 480, 490,
    ])

    proposed_edges = [
        (1, 22),
        (1, 44),
        (1, 66),
        (1, 88),

        (11, 22),
        (22, 33),
        (33, 44),
        (44, 55),
        (55, 66),
        (66, 77),
        (77, 88),
        (88, 11),

        (11, 110),
        (11, 250),
        (22, 120),
        (33, 130),
        (33, 150),
        (44, 160),
        (55, 170),
        (55, 190),
        (66, 200),
        (77, 210),
        (77, 230),
        (88, 240),

        (100, 110),
        (110, 120),
        (120, 130),
        (130, 140),
        (140, 150),
        (150, 160),
        (160, 170),
        (170, 180),
        (180, 190),
        (190, 200),
        (200, 210),
        (210, 220),
        (220, 230),
        (230, 240),
        (240, 250),
        (250, 100),

        (100, 310),
        (100, 530),
        (140, 350),
        (140, 370),
        (180, 410),
        (180, 430),
        (220, 470),
        (220, 490),

        (110, 320),
        (120, 330),
        (130, 340),
        (150, 380),
        (160, 390),
        (170, 400),
        (190, 440),

        (200, 450),
        (210, 460),
        (230, 500),
        (240, 510),
        (250, 520),

        (300, 310),
        (310, 320),
        (320, 330),
        (330, 340),
        (340, 350),
        (350, 360),
        (360, 370),
        (370, 380),
        (380, 390),
        (390, 400),

        (400, 410),
        (410, 420),
        (420, 430),
        (430, 440),
        (440, 450),
        (450, 460),
        (460, 470),
        (470, 480),
        (480, 490),
        (490, 500),

        (500, 510),
        (510, 520),
        (520, 530),
        (530, 300),
    ]

    for e in proposed_edges:
        edges = add_edge(edges, e[0], e[1])

    return vertices, edges


draw_graph = functools.partial(draw_graph, get_layout=get_layout)

FIG_SCALE = 1.2
LAYOUT_ROOT = 1


def main() -> None:
    hprint("Undirected matrix graph")
    V, E = build_graph()
    START = 1
    TARGET = 200

    M = set([START, TARGET])  # marked
    M_COLOR_MAP = {START: "cyan"}

    fig: plt.Figure = draw_graph(
        V, E, M,
        subplot=121,
        title="Start and target",
        marked_color_map=M_COLOR_MAP,
        layout_root=LAYOUT_ROOT,
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
    )


if __name__ == "__main__":
    main()
    plt.show()
