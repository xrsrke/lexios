import pytest

from lexios.solver.graph import Graph


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
