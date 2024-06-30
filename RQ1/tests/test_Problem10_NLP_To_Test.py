import pytest
from Problem10_GeneratedSolution import cherryPickup as max_cherries


@pytest.mark.parametrize("grid, expected", [
    # Basic examples provided in the problem statement
    ([[0,1,-1], [1,0,-1], [1,1,1]], 5),
    ([[1,1,-1], [1,-1,1], [-1,1,1]], 0),

    # Edge cases
    ([[1]], 1),  # Smallest grid possible, with only one cherry
    ([[0]], 0),  # Smallest grid possible, no cherries
    ([[-1]], 0),  # Smallest grid, impassable
    ([[1, -1], [-1, 1]], 0),  # No valid path through the grid

    # Larger grids with clear paths
    ([[0, 1, 1], [1, 0, 1], [1, 1, 1]], 8),  # Clear path available with multiple cherries
    ([[0, -1, 1], [1, 0, -1], [1, 1, 0]], 4),  # Partially blocked paths

    # Test maximum path scenarios
    ([[0, 0, 0, 0, 1],
      [0, -1, -1, 0, 1],
      [1, 1, -1, 0, 0],
      [0, -1, 1, 0, -1],
      [1, 1, 1, 0, 0]], 8),  # Complex path with some blocks

    # Path forces picking of minimal cherries
    ([[0, 0, 0, 0, 1],
      [1, -1, -1, 1, 0],
      [0, 1, -1, 0, 1],
      [1, 0, 1, 1, -1],
      [1, 1, 0, 0, 0]], 9)  # Optimal path to maximize cherries
])
def test_max_cherries(grid, expected):
    """
    Tests the `max_cherries` function to ensure it calculates the maximum number of cherries that can be collected.

    The tests cover:
    - Grids where paths are clear, partially blocked, and fully blocked.
    - Minimal grids to check behavior with smallest input size.
    - Larger, more complex grids to simulate realistic scenarios and ensure the pathfinding logic is robust.
    - Cases with no possible paths due to blocks to ensure graceful handling of no-solution scenarios.
    """
    assert max_cherries(grid) == expected, f"Expected {expected} cherries, but got a different number for grid {grid}"
