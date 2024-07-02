import pytest
from Problem9_GeneratedSolution import minPathSum


def test_non_straight_path():
    """
    Test a grid where the minimum path is non-straight.
    """
    grid = [
        [1, 10, 1],
        [1, 10, 1],
        [1, 1, 1]
    ]
    expected_sum = 5  # 1 -> 1 -> 1 -> 1 -> 1
    assert minPathSum(grid) == expected_sum, "Should calculate the correct minimum path sum for a non-straight path"

def test_single_row_grid():
    """
    Test a grid with only one row.
    """
    grid = [[1, 2, 3, 4]]
    expected_sum = 10  # 1 -> 2 -> 3 -> 4
    assert minPathSum(grid) == expected_sum, "Should calculate the correct minimum path sum for a single row grid"

def test_single_column_grid():
    """
    Test a grid with only one column.
    """
    grid = [[1], [2], [3], [4]]
    expected_sum = 10  # 1 -> 2 -> 3 -> 4
    assert minPathSum(grid) == expected_sum, "Should calculate the correct minimum path sum for a single column grid"

def test_negative_numbers_grid():
    """
    Test a grid that includes negative numbers.
    """
    grid = [
        [-1, -2, -3],
        [-2, -3, -4],
        [-3, -4, -5]
    ]
    expected_sum = -15  # Path through all cells
    assert minPathSum(grid) == expected_sum, "Should calculate the correct minimum path sum for a grid with negative numbers"
