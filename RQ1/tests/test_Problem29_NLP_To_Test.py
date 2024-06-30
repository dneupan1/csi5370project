import pytest
from solution import rotate as rotate_matrix  # Assuming the function 'rotate_matrix' is defined in 'solution.py'

@pytest.mark.parametrize("matrix, expected", [
    # Example 1: Simple 3x3 matrix
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[7, 4, 1], [8, 5, 2], [9, 6, 3]]),
    # Example 2: Larger 4x4 matrix
    ([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]], [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]),
    # Edge case: Single element
    ([[1]], [[1]]),
    # Edge case: 2x2 matrix
    ([[1, 2], [3, 4]], [[3, 1], [4, 2]]),
    # Larger 5x5 matrix
    ([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]],
     [[21, 16, 11, 6, 1], [22, 17, 12, 7, 2], [23, 18, 13, 8, 3], [24, 19, 14, 9, 4], [25, 20, 15, 10, 5]]),
    # Matrix with negative and zero
    ([[0, -1], [-1, 0]], [[-1, 0], [0, -1]]),
])
def test_rotate_matrix(matrix, expected):
    """
    Tests the rotate_matrix function with various n x n matrices to ensure it correctly rotates them by 90 degrees clockwise in-place.

    This test function verifies:
    - Proper rotation for small and large matrices.
    - Handling of edge cases like single-element and 2x2 matrices.
    - Rotation accuracy for matrices containing negative numbers and zeros.

    Args:
    matrix (list of list of int): The n x n matrix to be rotated.
    expected (list of list of int): The expected matrix after rotation.
    """
    rotate_matrix(matrix)
    assert matrix == expected, f"Test failed for matrix={matrix}. Expected {expected}, got {matrix}"

