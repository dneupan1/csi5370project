import pytest
from Problem32_GeneratedSolution import topological_sort as build_matrix  # Assuming the function 'build_matrix' is defined in 'solution.py'

@pytest.mark.parametrize("k, row_conditions, col_conditions, expected", [
    # Example 1: Possible configuration
    (3, [[1, 2], [3, 2]], [[2, 1], [3, 2]], [[3, 0, 0], [0, 0, 1], [0, 2, 0]]),
    # Example 2: Impossible configuration
    (3, [[1, 2], [2, 3], [3, 1], [2, 3]], [[2, 1]], []),
    # Simple valid configuration with no restrictions
    (2, [], [], [[1, 0], [0, 2]]),
    # Row conditions only, no column conditions
    (3, [[1, 2], [2, 3]], [], [[3, 0, 0], [2, 0, 0], [1, 0, 0]]),
    # Column conditions only, no row conditions
    (3, [], [[1, 2], [2, 3]], [[0, 0, 3], [0, 0, 2], [0, 0, 1]]),
    # Edge case: Single element
    (1, [], [], [[1]]),
    # Test larger k with feasible conditions
    (4, [[1, 2], [3, 4]], [[4, 1], [2, 3]], [[0, 0, 0, 4], [0, 0, 3, 0], [0, 1, 0, 0], [2, 0, 0, 0]]),
    # Test circular condition, should result in failure
    (4, [[1, 2], [2, 3], [3, 1]], [], []),
    # Test circular condition in columns, should result in failure
    (4, [], [[1, 2], [2, 3], [3, 1]], []),
    # Multiple valid outputs possible
    (3, [[1, 2]], [[2, 1]], [[0, 0, 3], [0, 2, 0], [1, 0, 0]]),
    # All elements in a single row and column respectively
    (3, [[1, 2], [2, 3]], [[1, 2], [2, 3]], [[3, 0, 0], [2, 0, 0], [1, 0, 0]])
])
def test_build_matrix(k, row_conditions, col_conditions, expected):
    """
    Tests the build_matrix function with various values of k, rowConditions, and colConditions to ensure it can construct a valid k x k matrix or return an empty matrix if conditions cannot be met.

    This function checks:
    - Handling of valid configurations that meet the specified row and column conditions.
    - Edge cases including empty conditions, single-element matrix, and potential circular dependencies.
    - Proper handling of configurations that result in no valid matrix due to conflicting conditions.

    Args:
    k (int): The size of the matrix and range of numbers.
    row_conditions (list of list of int): Conditions specifying row order constraints.
    col_conditions (list of list of int): Conditions specifying column order constraints.
    expected (list of list of int or empty list): Expected matrix or an empty list if no valid configuration exists.
    """
    result = build_matrix(k, row_conditions, col_conditions)
    assert result == expected, f"Test failed for k={k}, row_conditions={row_conditions}, col_conditions={col_conditions}. Expected {expected}, got {result}"
