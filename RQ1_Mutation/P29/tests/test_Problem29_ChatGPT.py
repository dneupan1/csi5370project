# test file
import pytest
from Problem29_GeneratedSolution import rotate  # Adjust this import based on your file structure

# Test with a 2x2 matrix
def test_rotate_2x2_matrix():
    matrix = [
        [1, 2],
        [3, 4]
    ]
    expected = [
        [3, 1],
        [4, 2]
    ]
    rotate(matrix)
    assert matrix == expected, "Failed to rotate a 2x2 matrix"

# Test with a 3x3 matrix
def test_rotate_3x3_matrix():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    expected = [
        [7, 4, 1],
        [8, 5, 2],
        [9, 6, 3]
    ]
    rotate(matrix)
    assert matrix == expected, "Failed to rotate a 3x3 matrix"

# Test with a 4x4 matrix to check for scalability and correct rotation in larger matrices
def test_rotate_4x4_matrix():
    matrix = [
        [ 5,  1,  9, 11],
        [ 2,  4,  8, 10],
        [13,  3,  6,  7],
        [15, 14, 12, 16]
    ]
    expected = [
        [15, 13,  2,  5],
        [14,  3,  4,  1],
        [12,  6,  8,  9],
        [16,  7, 10, 11]
    ]
    rotate(matrix)
    assert matrix == expected, "Failed to rotate a 4x4 matrix"

# Test with an empty matrix
def test_rotate_empty_matrix():
    matrix = []
    expected = []
    rotate(matrix)
    assert matrix == expected, "Failed with an empty matrix"

# Test with a single element matrix
def test_rotate_single_element_matrix():
    matrix = [[1]]
    expected = [[1]]  # A single-element matrix should remain unchanged
    rotate(matrix)
    assert matrix == expected, "Failed with a single element matrix"

# Test with a non-square matrix (although the problem statement specifies square matrices, this is to ensure robustness)
@pytest.mark.xfail(reason="Function designed for square matrices only")
def test_rotate_non_square_matrix():
    matrix = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    expected = [
        [4, 1],
        [5, 2],
        [6, 3]
    ]
    rotate(matrix)
    assert matrix == expected, "Failed with a non-square matrix"

