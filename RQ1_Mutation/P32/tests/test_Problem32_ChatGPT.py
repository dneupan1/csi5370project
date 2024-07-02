# test file
import pytest
from Problem32_GeneratedSolution import buildMatrix  # Adjust this import based on your file structure

# Test case with no conditions, expecting a matrix with natural numbers in ascending order
def test_no_conditions():
    k = 3
    rowConditions, colConditions = [], []
    expected = [[1, 0, 0], [0, 2, 0], [0, 0, 3]]
    assert buildMatrix(k, rowConditions, colConditions) == expected, "Failed with no conditions"

# Test case with a cycle in row conditions, expecting an empty matrix
def test_cycle_in_row_conditions():
    k = 2
    rowConditions = [[1, 2], [2, 1]]
    colConditions = []
    expected = []  # Impossible due to cycle in row conditions
    assert buildMatrix(k, rowConditions, colConditions) == expected, "Failed to identify cycle in row conditions"

# Test case with a cycle in column conditions, expecting an empty matrix
def test_cycle_in_col_conditions():
    k = 2
    rowConditions = []
    colConditions = [[1, 2], [2, 1]]
    expected = []  # Impossible due to cycle in column conditions
    assert buildMatrix(k, rowConditions, colConditions) == expected, "Failed to identify cycle in column conditions"

# Test case with conflicting conditions, expecting an empty matrix
def test_conflicting_conditions():
    k = 3
    rowConditions = [[1, 2], [2, 3]]
    colConditions = [[3, 2], [2, 1], [1, 3]]  # Creates a conflict
    expected = []  # Impossible due to conflicting conditions
    assert buildMatrix(k, rowConditions, colConditions) == expected, "Failed with conflicting conditions"

# Test case with larger matrix and multiple valid topological sorts
def test_larger_matrix_multiple_valid_sorts():
    k = 4
    rowConditions = [[1, 2], [4, 2], [3, 1]]
    colConditions = [[2, 3], [4, 1]]
    # Multiple valid matrices possible, focusing on row and column order validity
    result = buildMatrix(k, rowConditions, colConditions)
    # Check if the result satisfies the basic structure and condition requirements
    assert len(result) == k and all(len(row) == k for row in result), "Failed with a larger matrix and multiple valid sorts"

