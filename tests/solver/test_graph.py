import pytest

from lexios.solver.graph import Graph, ShortestPath, find_path_from_source_to_target


@pytest.fixture
def graph_with_weights():
    n_nodes = 5
    edges = [(0, 1, 4), (0, 4, 5), (1, 2, 6), (1, 3, 7), (1, 4, 8), (2, 3, 9), (3, 4, 10)]
    return Graph(n_nodes, edges, weighted=True)


def test_graph_with_weights(graph_with_weights):
    data = [[1, 4], [0, 2, 3, 4], [1, 3], [1, 2, 4], [0, 1, 3]]
    assert graph_with_weights.data == data

    weight = [[4, 5], [4, 6, 7, 8], [6, 9], [7, 9, 10], [5, 8, 10]]
    assert graph_with_weights.weight == weight


# @pytest.mark.parametrize(
#     "n_nodes, edges, data, weight",
#     [
#         (
#             5,
#             [(0, 1, 4), (0, 4, 5), (1, 2, 6), (1, 3, 7), (1, 4, 8), (2, 3, 9), (3, 4, 10)],
#             [[1, 4], [0, 2, 3, 4], [1, 3], [1, 2, 4], [0, 1, 3]],
#             [[4, 5], [4, 6, 7, 8], [6, 9], [7, 9, 10], [5, 8, 10]]
#         )
#     ]
# )
# def test_graph_with_weight(n_nodes, edges, data, weight):
#     graph = Graph(n_nodes, edges, weighted=True)

#     assert graph.data == data
#     assert graph.weight == weight


def test_find_edges(graph_with_weights):
    assert graph_with_weights.find_edges(3) == [1, 2, 4]
    assert graph_with_weights.find_weight(1, 2) == 6


@pytest.fixture
def graph_with_weight2():
    n_nodes = 9
    edges = [
        (0, 1, 3),
        (0, 3, 2),
        (0, 8, 4),
        (1, 7, 4),
        (2, 7, 2),
        (2, 3, 6),
        (2, 5, 1),
        (3, 4, 1),
        (4, 8, 8),
        (5, 6, 8),
    ]
    return Graph(n_nodes, edges, weighted=True)


def test_find_shortest_path(graph_with_weight2):

    shorest_path = ShortestPath(graph_with_weight2)
    length, path = shorest_path.find(2, 8)
    assert length == 15


def test_find_path_from_source_to_target(graph_with_weight2):
    shorest_path = ShortestPath(graph_with_weight2)
    _, path = shorest_path.find(2, 8)

    path_from_source_to_target = find_path_from_source_to_target(path)

    assert path_from_source_to_target == [2, 3, 4, 8]
