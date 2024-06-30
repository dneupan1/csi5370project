import pytest
from Problem11_GeneratedSolution import maximalPathQuality as max_quality_path


@pytest.mark.parametrize("values, edges, maxTime, expected", [
    # Basic example cases
    ([0, 32, 10, 43], [[0, 1, 10], [1, 2, 15], [0, 3, 10]], 49, 75),
    ([5, 10, 15, 20], [[0, 1, 10], [1, 2, 10], [0, 3, 10]], 30, 25),
    ([1, 2, 3, 4], [[0, 1, 10], [1, 2, 11], [2, 3, 12], [1, 3, 13]], 50, 7),

    # Edge cases
    ([1], [], 10, 1),  # Single node with no edges
    ([0, 0, 0], [[0, 1, 5], [1, 2, 5]], 10, 0),  # All nodes have zero values
    ([100, 200, 300], [[0, 1, 1], [1, 2, 1]], 1, 100),  # Time too short to move beyond first node
    ([100, 200, 300], [[0, 1, 1], [1, 2, 1]], 3, 600),  # Can visit all nodes within time limit

    # Testing loops and revisits
    ([10, 20, 30, 40], [[0, 1, 5], [1, 2, 5], [2, 0, 5], [0, 3, 10]], 25, 100),  # Can revisit nodes

    # Complex graph with multiple paths
    ([3, 4, 5, 6, 7], [[0, 1, 2], [1, 2, 3], [0, 3, 3], [3, 4, 4], [2, 4, 2]], 12, 25),
])
def test_max_quality_path(values, edges, maxTime, expected):
    """
    Test the `max_quality_path` function to ensure it calculates the maximum quality for valid paths.

    Args:
    values (list): The value of each node.
    edges (list of lists): Each sublist contains two nodes and the travel time between them.
    maxTime (int): Maximum allowable time for the round trip path.
    expected (int): Expected maximum quality value.

    The tests include:
    - Examples from the problem description.
    - Edge cases such as single node graphs, graphs where node values are zero, and time constraints that are restrictive.
    - Complex scenarios with multiple paths and loops to verify the function's ability to handle more intricate graph structures.
    """
    assert max_quality_path(values, edges, maxTime) == expected, f"Test failed with values={values}, edges={edges}, maxTime={maxTime}"
