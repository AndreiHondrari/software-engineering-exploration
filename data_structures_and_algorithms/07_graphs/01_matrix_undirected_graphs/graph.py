
import copy
from typing import Set, Tuple


def add_edge(
    edges: Set[Tuple[int, int]],
    node_a: int,
    node_b: int
) -> Set[Tuple[int, int]]:
    new_edges = copy.copy(edges)

    a = min(node_a, node_b)
    b = max(node_a, node_b)

    new_edges.add((a, b,))

    return new_edges


def delete(
    vertices: Set[int],
    edges: Set[Tuple[int, int]],
    value: int,
) -> Tuple[Set[int], Set[Tuple[int, int]]]:
    new_vertices = copy.copy(vertices)
    new_edges = copy.copy(edges)

    new_vertices.remove(value)

    dangling_edges: Set[Tuple[int, int]] = set(
        filter(lambda e: e[0] == value or e[1] == value, new_edges)
    )

    for dangling_edge in dangling_edges:
        new_edges.remove(dangling_edge)

    return new_vertices, new_edges


def get_edges(
    edges: Set[Tuple[int, int]],
    value: int,
) -> Set[Tuple[int, int]]:
    return set(
        filter(
            lambda e: e[0] == value or e[1] == value,
            edges
        )
    )


def get_neighbours(
    edges: Set[Tuple[int, int]],
    value: int,
) -> Set[int]:

    node_edges = get_edges(edges, value)

    neighbours: Set[int] = set()

    for e in node_edges:
        if e[0] == value:
            neighbours.add(e[1])
        else:
            neighbours.add(e[0])

    return neighbours
