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

    def __repr__(self):
        """Representation."""
        return "\n".join([f"{node}: {neighbors}" for node, neighbors in enumerate(self.data)])

    def __str__(self):
        """String."""
        return self.__repr__()
