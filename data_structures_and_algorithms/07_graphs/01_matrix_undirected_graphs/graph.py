
import copy
from collections import deque
from typing import Set, Tuple, Deque


def determine_edge(node_a: int, node_b: int) -> Tuple[int, int]:
    a = min(node_a, node_b)
    b = max(node_a, node_b)
    return (a, b,)


def add_edge(
    edges: Set[Tuple[int, int]],
    node_a: int,
    node_b: int
) -> Set[Tuple[int, int]]:
    new_edges = copy.copy(edges)
    new_edge = determine_edge(node_a, node_b)
    new_edges.add(new_edge)
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


def depth_first_search(
    vertices: Set[int],
    edges: Set[Tuple[int, int]],
    current: int,
    target: int,
    visited: Set[int] = set(),
    path: Set[Tuple[int, int]] = set()
) -> Tuple[bool, Set[Tuple[int, int]]]:
    if target not in vertices or current not in vertices:
        return False, set()

    # if target is reached then no need to continue the chase
    if current == target:
        return True, path

    updated_visited = copy.copy(visited)
    updated_visited.add(current)

    # try reaching the target through the neighbours
    adjacent_nodes = get_neighbours(edges, current)
    adjacent_unvisited_nodes = adjacent_nodes.difference(visited)

    for neighbour in adjacent_unvisited_nodes:
        path_to_neighbour = copy.copy(path)
        path_to_neighbour.add(determine_edge(current, neighbour))
        target_found, discovered_path = depth_first_search(
            vertices,
            edges,
            neighbour,
            target,
            updated_visited,
            path_to_neighbour,
        )

        if target_found:
            return True, discovered_path

    return False, set()


def breadth_first_search(
    vertices: Set[int],
    edges: Set[Tuple[int, int]],
    start: int,
    target: int,
) -> Tuple[bool, Set[Tuple[int, int]]]:

    if target not in vertices or start not in vertices:
        return False, set()

    search_edges: Set[Tuple[int, int]] = set()

    candidates: Deque[int] = deque()
    candidates.append(start)
    queued: Set[int] = set([start])

    while len(candidates) > 0:
        current_candidate = candidates.popleft()

        search_edges = search_edges.union(get_edges(edges, current_candidate))

        if current_candidate == target:
            return True, search_edges

        neighbours = get_neighbours(edges, current_candidate)
        unqueued_neighbours = neighbours.difference(queued)
        queued = queued.union(unqueued_neighbours)
        candidates.extend(unqueued_neighbours)

    return False, search_edges
