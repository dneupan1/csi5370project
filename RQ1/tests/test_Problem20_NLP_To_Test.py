import pytest
from Problem20_GeneratedSolution import trapRainWater  # Assuming the function 'trapRainWater' is defined in 'solution.py'

@pytest.mark.parametrize("heightMap, expected", [
    # Example 1: Small ponds in a 3x6 matrix
    ([[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4], [2, 3, 3, 2, 3, 1]], 4),
    # Example 2: Larger pond in a 5x5 matrix
    ([[3, 3, 3, 3, 3], [3, 2, 2, 2, 3], [3, 2, 1, 2, 3], [3, 2, 2, 2, 3], [3, 3, 3, 3, 3]], 10),
    # Edge case: Empty matrix should return 0
    ([], 0),
    # Edge case: Single row matrix should return 0
    ([[1, 2, 3, 4]], 0),
    # Edge case: Single column matrix should return 0
    ([[1], [2], [3], [4]], 0),
    # No trapping possible in flat matrix
    ([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 0),
    # Larger 4x4 matrix with complex trapping
    ([[5, 5, 5, 5], [5, 1, 1, 5], [5, 1, 1, 5], [5, 5, 5, 5]], 16),
    # Testing with varying heights
    ([[5, 3, 4, 5], [5, 1, 2, 5], [5, 3, 4, 5], [5, 5, 5, 5]], 9),
    # Edge case: Heights forming a funnel
    ([[5, 5, 5, 5, 5], [5, 1, 1, 1, 5], [5, 1, 1, 1, 5], [5, 1, 1, 1, 5], [5, 5, 5, 5, 5]], 48)
])
def test_trapRainWater(heightMap, expected):
    """
    Tests the trapRainWater function with various 2D elevation maps to ensure it correctly calculates the volume of water trapped.

    This test function verifies:
    - Proper handling of different matrix sizes and configurations.
    - Handling of edge cases such as empty matrices, single row/column matrices, and matrices where no water can be trapped.
    - Accurate calculation of trapped water in complex scenarios with varying heights and potential ponds.

    Args:
    heightMap (list of list of int): The 2D elevation map representing heights.
    expected (int): The expected volume of water that can be trapped.
    """
    result = trapRainWater(heightMap)
    assert result == expected, f"Test failed for heightMap={heightMap}. Expected {expected}, got {result}"
