import pytest
from Problem9_GeneratedSolution import minPathSum as min_path_sum

@pytest.mark.parametrize("grid, expected", [
    ([[1, 3, 1], [1, 5, 1], [4, 2, 1]], 7),  # Standard case with multiple paths
    ([[1, 2, 3], [4, 5, 6]], 12),            # Rectangular grid
    ([[1]], 1),                              # Single element grid
    ([[1, 2], [3, 4]], 7),                   # Small 2x2 grid
    ([[1, 100], [1, 1]], 3),                 # Path choice significantly affects sum
    ([[2, 2, 2], [2, 2, 2], [2, 2, 2]], 12), # Uniform values
    ([[1, 2, 3], [4, 1, 6], [7, 8, 1]], 8),  # Path with minimal sum in the middle
    ([[1, 10, 1], [1, 1, 10], [10, 1, 1]], 5) # Path avoiding high values
])
def test_min_path_sum(grid, expected):
    """
    Test the `min_path_sum` function to ensure it correctly calculates the minimum path sum from the top-left to the bottom-right of a grid.

    Args:
    grid (List[List[int]]): The grid of non-negative integers.
    expected (int): The expected minimum path sum.

    The test covers:
    - Various grid sizes and configurations.
    - Different path choices impacting the sum.
    - Grids with uniform values to check consistent path calculations.
    - Small grids to handle edge cases.
    """
    assert min_path_sum(grid) == expected, f"Failed for grid {grid} with expected sum {expected}"
