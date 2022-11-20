"""Implementation of graph data structures."""

from typing import List, Tuple, Union

Weight = Union[int, float]
Edge = Union[Tuple[str, str], Tuple[int, int, Weight]]
Node = Union[str, int]


class Graph:
    """Implementation of graph data structure."""

    def __init__(self, n_nodes: int, edges: List[Edge], weighted: bool = False):
        """Initialize a graph."""
        self.n_nodes = n_nodes
        self.weighted = weighted
        self.data: List[List[Node]] = [[] for _ in range(n_nodes)]
        self.weight: List[Weight] = [[] for _ in range(n_nodes)]

        for edge in edges:
            if self.weight:
                node1, node2, weight = edge
                self.weight[node1].append(weight)
                self.weight[node2].append(weight)
            else:
                node1, node2 = edge

            self.data[node1].append(node2)
            self.data[node2].append(node1)

    def find_edges(self, node: Node) -> List[Node]:
        """Return all the neighbors nodes of a node."""
        return self.data[node]

    # def find_weights(self, node: Node):
    #     return self.weight[node]

    def find_weight(self, node1: Node, node2: Node) -> Weight:
        """Return the weight between two nodes."""
        idx = [i for i, node in enumerate(self.find_edges(node1)) if node == node2]
        return self.weight[node1][idx[0]]

    def find_weights(self, node: Node) -> List[List[Weight]]:
        """List all the weights that associated with a node."""
        return self.weight[node]

    def __repr__(self):
        """Representation."""
        return "\n".join([f"{node}: {neighbors}" for node, neighbors in enumerate(self.data)])

    def __str__(self):
        """String."""
        return self.__repr__()


INFINITY = float("inf")


class ShortestPath:
    """Implementation of the shortest path algorithm."""

    def __init__(self, graph: Graph):
        """Initialize the shortest path algorithm."""
        self.graph = graph
        self.visited = [False] * len(graph.data)
        self.parent = [None] * len(graph.data)
        self.distance = [INFINITY] * len(graph.data)
        self.queue = []

    def find(self, source: Node, target: Node) -> Tuple[int, List[int]]:
        """Find the shortest path from source to target."""
        self.distance[source] = 0
        self.distance[source] = 0
        self.queue.append(source)

        idx = 0

        while idx < len(self.queue) and not self.visited[target]:
            current = self.queue[idx]
            self.visited[current] = True
            idx += 1

            # update the distance of all the neighbors
            self.update_distance(current)

            # find the unvisited node with the smallest distance
            next_node = self.pick_next_node()
            if next_node:
                self.queue.append(next_node)

        return self.distance[target], self.parent

    def update_distance(self, current: Node):
        """Update the distance of the current node to all its neighbors."""
        neighbors = self.graph.find_edges(current)
        weights = self.graph.find_weights(current)

        for i, node in enumerate(neighbors):
            weight = weights[i]

            if self.distance[current] + weight < self.distance[node]:
                self.distance[node] = self.distance[current] + weight
                if self.parent:
                    self.parent[node] = current

    def pick_next_node(self) -> Node:
        """Pick the next unvisited node at the smallest distance."""
        min_distance = float("inf")
        min_node = None

        for node in range(len(self.distance)):
            if not self.visited[node] and self.distance[node] < min_distance:
                min_node = node
                min_distance = self.distance[node]

        return min_node


def find_path_from_source_to_target(path: List[Node]) -> List[Node]:
    """Find the path from the source to the target given the path from ShortestPath class."""
    path_dict = {}

    for i, node in enumerate(path):
        path_dict[i] = node

    target = list(path_dict.keys())[-1]
    parent = target

    target_to_source = [target]

    while path_dict[parent]:
        parent = path_dict[parent]
        target_to_source.append(parent)

    source_to_target = list(reversed(target_to_source))
    return source_to_target
